from rest_framework import permissions

class AllowCompleteAndVerified(permissions.BasePermission):
    message = "Profile needs to be filled and account must be verified"

    def has_permission(self,request,view):
        try:
            if request.user.profile.is_profile_complete:
                if request.user.verified_account.is_verified:
                    return True
        except:
            return False
        return False