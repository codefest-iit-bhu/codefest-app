from firebase_admin import auth
from rest_framework.status import HTTP_422_UNPROCESSABLE_ENTITY
from rest_framework.exceptions import ValidationError

class FirebaseAPI:

    @classmethod
    def verify_id_token(cls, token):
        try:
            decoded_token = auth.verify_id_token(token)
            return decoded_token
        except ValueError:
            raise ValidationError(
                'Invalid Firebase ID Token.', HTTP_422_UNPROCESSABLE_ENTITY)

    @classmethod
    def get_provider_uid(cls, jwt, provider):
        return jwt['firebase']['identities'][provider][0]

    @classmethod
    def get_provider(cls, jwt):
        """
        Parses Firebase-provided JWT and returns the OAuth2 provider type

        Arguments:
            jwt {str} -- Valid and decoded JWT provided by Firebase

        Returns:
            One of the following:
            google.com
            facebook.com
            github.com
            password
        """
        provider = jwt['firebase']['sign_in_provider']
        from .models import VerifiedAccount
        if provider not in [VerifiedAccount.AUTH_FACEBOOK_PROVIDER, 
        VerifiedAccount.AUTH_EMAIL_PROVIDER, 
        VerifiedAccount.AUTH_GITHUB_PROVIDER, 
        VerifiedAccount.AUTH_GOOGLE_PROVIDER]:
            raise ValidationError('Given provider not supported')
        return provider


    @classmethod
    def delete_user_by_uid(cls, uid):
        auth.delete_user(uid)

    @classmethod
    def get_email_confirmation_status(cls,uid):
        return auth.get_user(uid).email_verified
        

