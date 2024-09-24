from pywebio import start_server
from pywebio.output import put_text, put_button, put_markdown, put_html
from pywebio.input import input, TEXT

def main():
    put_html("<h1>Welcome to Our Website</h1>")
    put_html("<p>We are glad to have you here. Please explore our features and services.</p>")
    
    put_markdown("### Contact Us")
    name = input("What's your name?", type=TEXT)
    email = input("What's your email?", type=TEXT)
    message = input("Your message", type=TEXT)
    
    put_button("Submit", onclick=lambda: put_text(f"Thank you, {name}! We Noted {email} We have received your message."))

if __name__ == "__main__":
    start_server(main, port=8080)
