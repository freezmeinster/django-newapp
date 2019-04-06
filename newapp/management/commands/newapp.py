from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    create new app.
    """
    help = __doc__
    args = '<function arg arg ...>'

    def add_arguments(self, parser):
        parser.add_argument('--queue', '-q', dest='queue', default='default',
                            help='Specify the queue [default]')
        parser.add_argument('--timeout', '-t', type=int, dest='timeout', 
                            help='A timeout in seconds')

    def handle(self, *args, **options):
        """
        Queues the function given with the first argument with the
        parameters given with the rest of the argument list.
        """
        print("New Apps was created")