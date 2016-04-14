from app_name import create_app

if __name__ == '__main__':
    application = create_app()
    application.run(
        host=application.config['HOST'],
        port=application.config['PORT']
    )
