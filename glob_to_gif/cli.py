"""Console script for glob_to_gif."""
import sys
import click
import glob
import imageio

@click.command()
@click.argument('glob',type=str,nargs=1)
@click.argument('out_file',type=str,nargs=1)
def main(**kwargs):
    """Console script for glob_to_gif."""

    anim_file = kwargs['out_file']

    with imageio.get_writer(anim_file, mode="I") as writer:
        glob_str = kwargs['glob']

        filenames = glob.glob(glob_str)

        print(f'Making gif from {len(filenames)} files found with {glob_str}')

        filenames = sorted(filenames)
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
        image = imageio.imread(filename)
        writer.append_data(image)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
