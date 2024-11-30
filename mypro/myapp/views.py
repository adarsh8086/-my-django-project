from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem ,Product, Purchase
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.views.generic import DetailView
from .models import Product,Purchase
from .models import Order, OrderItem
from django.contrib import messages
from .forms import UserLoginForm


# Create your views here.



def Shop(request):
   
    return render(request, "shop.html")

def men_category_view(request):
    return render(request, 'Men_category.html')  

def women_category_view(request):
    return render(request, 'women_category.html')  

def about_us_view(request):
    return render(request, 'About-us.html')

def home(request):
    return render(request, 'home.html')


@login_required(login_url='/login/')  # Redirect to login if not authenticated
def buy_now(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user 
    
    Purchase.objects.create(
        user=user,
        product=product,
        quantity=1 
    )
    return redirect('checkout', product_id=product.id)












def checkout(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Fetch the CartItem
    cart_item = CartItem.objects.filter(user=request.user, product=product).first()

    if request.method == 'POST':
        # Get the updated quantity from the form
        quantity = int(request.POST.get('quantity', cart_item.quantity if cart_item else 1))

        # Update the CartItem in the database
        if cart_item:
            cart_item.quantity = quantity
            cart_item.save()

        # Re-fetch the updated CartItem from the database
        cart_item.refresh_from_db()

    # Use the updated quantity
    quantity = cart_item.quantity if cart_item else 1
    total_amount = product.price * quantity

    # Prepare order items
    order_items = [{'product': product, 'quantity': quantity, 'price': product.price}]

    context = {
        'order_items': order_items,
        'total_amount': total_amount,
        'quantity': quantity,
    }

    return render(request, 'checkout.html', context)








class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'





   

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')
 

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'cart.html', context)




class CustomLoginView(LoginView):
    template_name = 'Login.html'
    authentication_form = UserLoginForm  # Use the custom login form





def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'Register.html', {'form': form})








@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart') 













@login_required
def confirm_order(request):
    if request.method == 'POST':
        # Get shipping details from the form
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        product_id = request.POST.get('product_id')
        payment_method = request.POST.get('payment_method')
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not provided

        # Create the full shipping address
        shipping_address = f"{address}, {city}, {state}, {zip_code}"

        # Handle the specific product purchase
        if product_id:
            product = Product.objects.get(id=product_id)

            

             # Check and update quantity in the cart
            cart_item = CartItem.objects.filter(user=request.user, product=product).first()
            if cart_item:
                # Update cart quantity with form data
                if quantity != cart_item.quantity:
                    cart_item.quantity = quantity
                    cart_item.save()
                
                quantity = cart_item.quantity  # Use updated quantity
            else:
                quantity = quantity  

            
            total_amount = product.price * quantity

            # Create a new Order
            order = Order.objects.create(
                user=request.user,
                total_amount=total_amount,
                shipping_address=shipping_address,
                payment_status='Pending',
                payment_method=payment_method
            )

            # Create the order item
            order_item = OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )

            # Create the Purchase entry
            Purchase.objects.create(
                user=request.user,
                product=product,
                quantity=quantity,
                order=order 
            )

            # Remove the item from the cart
            CartItem.objects.filter(user=request.user, product=product).delete()

            # Pass the data to the template
            context = {
                'order_items': [order_item],
                'total_amount': total_amount,
                'shipping_address': shipping_address,
                'payment_method': payment_method
            }

            # Redirect based on payment method
            if payment_method == 'COD':
            
                print("Order confirmed with Cash on Delivery.")
            elif payment_method == 'GPay':
            
                return redirect('https://pay.google.com')
            elif payment_method == 'PhonePe':
                
                return redirect('https://www.phonepe.com')
            elif payment_method == 'Card':
                
                return redirect('https://your_card_payment_gateway.com')  

            return render(request, 'order_confirmation.html', context)

    return redirect('shop')







@login_required
def view_ordered_items(request):
    orders = Order.objects.prefetch_related('order_items__product').filter(user=request.user)
    return render(request, 'ordered_items.html', {'orders': orders})









def clear_orders(request):
    if request.method == "POST":
        # Assuming you want to clear orders for the current user
        orders = Order.objects.filter(user=request.user)
        orders.delete()
        messages.success(request, "All orders have been cleared.")
        return redirect('view_ordered_items')  # Redirect to the page where orders are displayed
    return redirect('view_ordered_items')







def cancel_last_order(request, order_id):
    if request.method == 'POST':
        # Get the order by its ID (including related order items)
        order = get_object_or_404(Order, id=order_id)

        if order:
            # Delete the entire order (this will delete the related order items as well, if related by a foreign key)
            order.delete()
            messages.success(request, "Your order has been canceled.")
        else:
            messages.error(request, "This order does not exist.")

        return redirect('view_ordered_items')  # Redirect to the page where orders are displayed

    return redirect('view_ordered_items')



