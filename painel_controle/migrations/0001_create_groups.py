from django.db import migrations


def criar_grupos(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    grupos = {
        'client': [],

        'admin_staff': [
            # Jogos e categorias
            'add_jogo', 'change_jogo', 'view_jogo',
            'add_categoria', 'change_categoria', 'view_categoria',

            # Imagens extras
            'add_imagemextra', 'change_imagemextra', 'view_imagemextra',

            # Compras
            'view_compra',
        ],

        'hard_deleter': [
            'delete_jogo',
            'delete_categoria',
            'delete_compra',
            'delete_imagemextra',
        ],

        'user_manager': [
            # Usuários
            'add_user', 'change_user', 'view_user',

            # Grupos e permissões
            'add_group', 'change_group', 'view_group',
            'add_permission', 'change_permission', 'view_permission',
        ],
    }

    for nome_grupo, perms_codename in grupos.items():
        grupo, _ = Group.objects.get_or_create(name=nome_grupo)

        if perms_codename:
            permissoes = Permission.objects.filter(codename__in=perms_codename)
            grupo.permissions.set(permissoes)


def remover_grupos(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(
        name__in=['client', 'admin_staff', 'hard_deleter', 'user_manager']
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0001_initial'),  # ajuste se necessário
    ]

    operations = [
        migrations.RunPython(criar_grupos, remover_grupos),
    ]
