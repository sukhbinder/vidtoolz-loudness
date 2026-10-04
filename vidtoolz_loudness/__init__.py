import vidtoolz
from vidtoolz.utils import determine_output_path

import subprocess
import sys


def normalize_audio(
    input_file, output_file, loudness=-16, true_peak=-1.5, lra=11, sample_rate="44.1k"
):
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        input_file,
        "-af",
        f"loudnorm=I={loudness}:TP={true_peak}:LRA={lra}",
        "-ar",
        f"{sample_rate}",
        output_file,
    ]

    print(f"Running command:\n{' '.join(cmd)}\n")
    try:
        subprocess.run(cmd, check=True)
        print(f"Normalization complete: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during normalization: {e}")
        sys.exit(1)


def create_parser(subparser):
    parser = subparser.add_parser(
        "loudness", description="Use EBU R128 Loudness Normalization with ffmpeg"
    )
    # Add subprser arguments here.
    parser.add_argument("input", type=str, help="Path to the input video file.")
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="Path to save the output video with the shake effect.",
    )
    parser.add_argument(
        "-l",
        "--loudness",
        type=float,
        default=-16,
        help="Target integrated loudness in LUFS (default: -16)",
    )
    parser.add_argument(
        "-tp",
        "--true-peak",
        type=float,
        default=-1.5,
        help="True peak limit in dB (default: -1.5)",
    )
    parser.add_argument(
        "--lra", type=int, default=11, help="Loudness range target (default: 11)"
    )
    parser.add_argument(
        "-sr",
        "--sample-rate",
        type=str,
        default="44.1k",
        help="Audio sample rate (default: 44.1k)",
    )
    return parser


class ViztoolzPlugin:
    """Use EBU R128 Loudness Normalization with ffmpeg"""

    __name__ = "loudness"

    @vidtoolz.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)

    def run(self, args):
        # add actual call here
        output = determine_output_path(args.input, args.output, "loudnorm")
        normalize_audio(
            args.input,
            output,
            args.loudness,
            args.true_peak,
            args.lra,
            args.sample_rate,
        )

    def hello(self, args):
        # this routine will be called when "vidtoolz "loudness is called."
        print("Hello! This is an example ``vidtoolz`` plugin.")


loudness_plugin = ViztoolzPlugin()
