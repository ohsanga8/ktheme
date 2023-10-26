# Generated by Django 4.1.3 on 2023-10-23 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("make_ktheme", "0015_ktheme_bg_color_ktheme_input_bg_color_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ktheme",
            name="bg_color",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="dir_path",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="input_bg_color",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="main_text_color",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="point_text_color",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="r_1_b",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="r_1_l",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="r_1_r",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="r_1_t",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="r_1_x",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="r_1_y",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="r_2_b",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="r_2_l",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="r_2_r",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="r_2_t",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="r_2_x",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="r_2_y",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="receive_text_color",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="s_1_b",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="s_1_l",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="s_1_r",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="s_1_t",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="s_1_x",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="s_1_y",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="s_2_b",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="s_2_l",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="s_2_r",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="s_2_t",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="s_2_x",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="s_2_y",
        ),
        migrations.RemoveField(
            model_name="ktheme",
            name="send_text_color",
        ),
        migrations.AddField(
            model_name="ktheme",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="ktheme",
            name="theme_id",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="ktheme",
            name="theme_name",
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name="CssColor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bg_color", models.CharField(default="#FFFFFF", max_length=7)),
                ("main_text_color", models.CharField(default="#000000", max_length=7)),
                ("point_text_color", models.CharField(default="#FFC0CB", max_length=7)),
                ("input_bg_color", models.CharField(default="#D3D3D3", max_length=7)),
                ("send_text_color", models.CharField(default="#A9A9A9", max_length=7)),
                (
                    "receive_text_color",
                    models.CharField(default="#808080", max_length=7),
                ),
                (
                    "ktheme",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="make_ktheme.ktheme",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CssBubble",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("s_1_x", models.PositiveIntegerField(default=17)),
                ("s_1_y", models.PositiveIntegerField(default=17)),
                ("s_1_t", models.PositiveIntegerField(default=10)),
                ("s_1_l", models.PositiveIntegerField(default=11)),
                ("s_1_b", models.PositiveIntegerField(default=9)),
                ("s_1_r", models.PositiveIntegerField(default=17)),
                ("s_2_x", models.PositiveIntegerField(default=17)),
                ("s_2_y", models.PositiveIntegerField(default=17)),
                ("s_2_t", models.PositiveIntegerField(default=10)),
                ("s_2_l", models.PositiveIntegerField(default=11)),
                ("s_2_b", models.PositiveIntegerField(default=9)),
                ("s_2_r", models.PositiveIntegerField(default=17)),
                ("r_1_x", models.PositiveIntegerField(default=20)),
                ("r_1_y", models.PositiveIntegerField(default=17)),
                ("r_1_t", models.PositiveIntegerField(default=10)),
                ("r_1_l", models.PositiveIntegerField(default=17)),
                ("r_1_b", models.PositiveIntegerField(default=9)),
                ("r_1_r", models.PositiveIntegerField(default=11)),
                ("r_2_x", models.PositiveIntegerField(default=20)),
                ("r_2_y", models.PositiveIntegerField(default=17)),
                ("r_2_t", models.PositiveIntegerField(default=10)),
                ("r_2_l", models.PositiveIntegerField(default=17)),
                ("r_2_b", models.PositiveIntegerField(default=9)),
                ("r_2_r", models.PositiveIntegerField(default=11)),
                (
                    "ktheme",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="make_ktheme.ktheme",
                    ),
                ),
            ],
        ),
    ]