



function showOrderConfirmationAlert(event) {
    event.preventDefault(); // Prevent the default form submission
    
    
    const paymentMethod = document.querySelector('input[name="payment_method"]:checked');
    
    // Check if the payment method is Cash on Delivery (COD)
    if (paymentMethod && paymentMethod.value === 'COD') {
        
        alert('Your order has been confirmed!');
    }

    
    event.target.submit(); // This triggers the form submission after the alert
}






// for subscription newsletter


function showPopup(event) {
    const emailField = document.querySelector('input[name="email"]');
    const errorMessage = document.getElementById('error-message');
    const emailValue = emailField.value.trim(); // Get the value of the email field and trim whitespace

    if (emailValue === "") {
        event.preventDefault(); // Prevent form submission
        errorMessage.style.display = 'block'; // Show the error message
        
    } else {
        errorMessage.style.display = 'none'; // Hide the error message if email is valid
        alert("Thank you for subscribing!");
        event.target.submit(); // Submit the form after showing the alert
    }
}



// for cancel booking


function confirmCancel() {
    return confirm("Are you sure you want to cancel this booking?");
}









// Function to check if the cancel button should be visible in orderd items

function hideCancelButtons() {
    const forms = document.querySelectorAll('.cancel-order-form');
    
    forms.forEach(form => {
        const orderDateStr = form.dataset.orderDate;
        if (orderDateStr) {
            const orderDate = new Date(orderDateStr); // Parse order date
            const currentTime = new Date(); // Current date and time
            const timeDifference = currentTime - orderDate; // Time difference in milliseconds
            
            // Convert 24 hours to milliseconds (24 * 60 * 60 * 1000)
            const oneDayInMillis = 24 * 60 * 60 * 1000;

            // Hide the button if more than 24 hours have passed
            if (timeDifference > oneDayInMillis) {
                const button = form.querySelector('.cancel-button');
                if (button) {
                    button.style.display = 'none';
                }
            }
        }
    });
}

// Call the function after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', hideCancelButtons);






// logout alert

function showLogoutAlert() {
    alert("You have been logged out successfully.");
}