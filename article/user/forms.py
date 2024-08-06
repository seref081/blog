from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı")
    password = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)


class RegisterForm (forms.Form):
    username=forms.CharField(max_length=50, label="Kullanıcı Adı")
    password=forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=20, label="Parolayı doğrula", widget=forms.PasswordInput)

    def clean(self): #django bu fonksiyonun kullanılmasını tavsiye ediyor
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")

        if password and confirm and password !=confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor...")

        values={ #yukarıdaki password ve username eşleşiyorsa sözlük içinde şu döngü verilmeli
            "username":username,
            "password":password
        }
        return values

