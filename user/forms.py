from django import forms


class LoginForm(forms.Form):
    user_account = forms.CharField(label="아이디", max_length=20)
    password = forms.CharField(label="패스워드", max_length=40, widget=forms.PasswordInput())


class JoinForm(forms.Form):
    user_account = forms.CharField(label='유저 계정', max_length=20)
    password = forms.CharField(label='유저 비밀번호', max_length=40, widget=forms.PasswordInput())
    password2 = forms.CharField(label='비밀번호 체크', max_length=40, widget=forms.PasswordInput())
    user_name = forms.CharField(label='유저 이름', max_length=10)
    nickname = forms.CharField(label='유저 닉네임', max_length=10)
    user_phone = forms.CharField(label='유저 핸드폰 번호', max_length=15)
    user_email = forms.EmailField(label='유저 이메일', max_length=30)


