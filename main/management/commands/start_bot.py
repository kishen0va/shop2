from django.core.management.base import BaseCommand

from main.bot import bot


class Command(BaseCommand):
    help = 'Start bot'

    def handle(self, *args, **options):
        bot.polling(none_stop=True)
