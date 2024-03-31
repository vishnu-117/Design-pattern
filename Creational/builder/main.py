from email_builder import EmailBuilder

def main():
    email_message = (
        EmailBuilder()
        .add_from('vtu@gmail.com')
        .add_to('ttu@gmail.com')
        .add_cc('kkr@gmail.com')
        .with_subject('The builder pattern tutorial')
        .with_body('Learning buider pattern')
        .add_attachment('vtu.pdf')
        .build()
    )
    email_message.send()

if __name__ == "__main__":
    main()