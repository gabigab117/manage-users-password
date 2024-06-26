# Session du 1er mai 2024 (talk Docstring.fr)

https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.views.PasswordChangeView

## Reverse et Reverse Lazy (Français)

https://twitter.com/GabrielTrouve/status/1784654086941368655

Lorsque vous utilisez reverse dans une fonction, le code n'est exécuté que lorsque la fonction est appelée. Donc reverse
traduit le nom de la vue en URL à ce moment-là.

Cependant, lorsqu'une classe est définie, les attributs de classe sont évalués immédiatement. Donc si vous essayez
d'utiliser reverse comme valeur par défaut pour un attribut de classe, Django va essayer de traduire le nom de la vue en
URL immédiatement au moment de l'importation du module, et non au moment où une instance de la classe est créée.

Cela signifie que les attributs de la classe existent dès que la classe est définie, bien avant qu'une instance de
celle-ci soit créée.
Les attributs de classe sont évalués et assignés dès que Python interprète la définition de la classe, même si aucune
instance de la classe n'est encore créée. C'est différent des attributs d'instance, qui ne sont évalués et assignés que
lorsqu'une instance spécifique de la classe est créée.

## Vue activate (exceptions) (Français)

- TypeError : Cette exception pourrait être levée si une fonction est appliquée à une valeur de mauvais type. Par exemple,
si uidb64 n'est pas une chaîne qui peut être décryptée en base 64, urlsafe_base64_decode(uidb64) lèvera cette exception.

- ValueError : Cette exception pourrait être levée si urlsafe_base64_decode(uidb64) retourne une valeur qui ne correspond
pas à une clé primaire d'utilisateur valide dans la base de données. Par exemple, si la décode de uidb64 donne une
chaîne au lieu d'un nombre.

- OverflowError : Cette exception serait levée si urlsafe_base64_decode(uidb64) retourne un nombre trop grand pour la clé
primaire d'un utilisateur.

- user.DoesNotExist : Cette exception est levée si aucun utilisateur correspondant à l'uid décodé n'est trouvé dans la
base de données. C'est-à-dire que l'utilisateur avec l'ID spécifié n'existe pas.

## Project

### Overview

This Django application demonstrates how to implement a system for updating passwords and resetting them. Furthermore,
it illustrates the way to construct a user account activation feature.

### 1. Password Update

The password update system utilizes Django's inbuilt views: PasswordChangeView and PasswordChangeDoneView.

### 2. Password Reset

The password reset system utilizes these Django's inbuilt views: PasswordResetView, PasswordResetDoneView,
PasswordResetConfirmView, and PasswordResetCompleteView.

### 3. User Account Activation

This application also includes a user account activation feature using token authentication. It generates the token
using PasswordResetTokenGenerator.

### Email Host Password

The EMAIL_HOST_PASSWORD should be defined within your .env file.
