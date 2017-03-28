from cloudinary.uploader import upload


def handle_uploads(file):
    response = upload(file, resource_type='raw')
    return response['secure_url']
