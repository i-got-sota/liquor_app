from allauth.account.forms import (LoginForm, SignupForm, 
                                   ResetPasswordKeyForm, ResetPasswordForm)


from .models import CustomUser


# ログイン用フォーム
class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

# サインアップ用フォーム
class MySignupForm(SignupForm):
    """ Userクラス用フォーム """
    class Meta:
        model = CustomUser

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'ユーザー名'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレス'
        self.fields['password1'].widget.attrs['placeholder'] = 'パスワード'
        self.fields['password2'].widget.attrs['placeholder'] = 'パスワード(確認用)'

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

# パスワードリセット(変更用フォーム)
class MyResetPasswordKeyForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].widget.attrs['placeholder'] ='パスワード(確認用)'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

# パスワードリセット(メール送信用フォーム)
class MyResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'