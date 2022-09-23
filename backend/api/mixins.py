from rest_framework import permissions
from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixins():
    permission_classes = [permissions.IsAdminUser , IsStaffEditorPermission]
