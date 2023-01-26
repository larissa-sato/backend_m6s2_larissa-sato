
def handle_uploaded(f):
    with open('cnab.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)