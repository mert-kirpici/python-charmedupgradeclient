import logging

from osc_lib.command import command

logger = logging.getLogger(__name__)

class UpgradePrep(command.Command):

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument("dummy", help="A dummy argument")
        return parser

    def take_action(self, parser_args):
        logger.warning(f"upgrade prep called with {parser_args.dummy}")
