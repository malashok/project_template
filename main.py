from app.io import input, output


def main():
    from_console = input.input_from_console()
    from_file = input.input_from_file("data/example.txt")
    from_file_pd = input.input_from_file_pd("data/example.txt")
    print()
    output.output_to_console("from console: " + from_console)
    output.output_to_console("from file: " + from_file)
    output.output_to_console("from file 2 (pandas): " + str(from_file_pd))
    print()
    output.output_to_file("data/console_out.txt", from_console)
    output.output_to_file("data/file_out.txt", from_file)
    output.output_to_file_pd("data/file_out_pd.txt", from_file_pd)


if __name__ == "__main__":
    main()
