from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_payment_receipt(customer_name, amount_paid, payment_method):
    # Create a PDF document
    c = canvas.Canvas("payment_receipt.pdf", pagesize=letter)

    # Set up the title and receipt information
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "Payment Receipt")
    c.setFont("Helvetica", 12)
    c.drawString(100, 730, "Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    c.drawString(100, 710, "Customer Name: " + customer_name)
    c.drawString(100, 690, "Amount Paid: $" + str(amount_paid))
    c.drawString(100, 670, "Payment Method: " + payment_method)

    # Add a thank you message
    c.setFont("Helvetica", 12)
    c.drawString(100, 630, "Thank you for your payment!")

    # Save the PDF
    c.save()

# Example usage
customer_name = "John Doe"
amount_paid = 100.00
payment_method = "Credit Card"

generate_payment_receipt(customer_name, amount_paid, payment_method)
