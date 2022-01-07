from .import_data_from_profit_chart_into_metatrader import import_data_from_profit_chart_into_metatrader


def import_data_from_profit_chart(args):
    if args.destination is None:
        print("Missing --destination parameter")
        sys.exit(1)
    if args.source is None:
        print("Missing --source parameter")
        sys.exit(1)
    import_data_from_profit_chart_into_metatrader(
        args.source, args.destination, args.initialdate)
