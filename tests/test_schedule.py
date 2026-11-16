import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which("jekyll"), "Jekyll is required to build the test site")
class FractionalScheduleDurationTest(unittest.TestCase):
    def test_ninety_minute_event_overlaps_on_half_hour_grid(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            source = Path(temporary_directory) / "source"
            destination = Path(temporary_directory) / "site"
            shutil.copytree(
                ROOT,
                source,
                ignore=shutil.ignore_patterns(".git", "_site", "__pycache__"),
            )
            for event_file in (source / "_events").iterdir():
                event_file.unlink()
            (source / "_events" / "ninety-minute-event.md").write_text(
                "---\n"
                "title: Ninety-minute event\n"
                "kind: panel\n"
                "category: Test\n"
                "day: 1\n"
                "slot: 11\n"
                "length: 1.5\n"
                "time: 11:00–12:30\n"
                "---\n"
            )
            (source / "_events" / "overlapping-event.md").write_text(
                "---\n"
                "title: Overlapping event\n"
                "kind: seminar\n"
                "category: Test\n"
                "day: 1\n"
                "slot: 12\n"
                "length: 1\n"
                "time: 12:00–13:00\n"
                "---\n"
            )

            subprocess.run(
                [
                    "jekyll",
                    "build",
                    "--source",
                    str(source),
                    "--destination",
                    str(destination),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            schedule = (destination / "schedule" / "index.html").read_text()

        self.assertIn("--event-columns: 2", schedule)
        self.assertIn("--slot: 3; --length: 3", schedule)
        self.assertIn("--slot: 5; --length: 2", schedule)
        self.assertIn('class="event-card panel overlapping"', schedule)
        self.assertIn('class="event-card seminar overlapping"', schedule)


if __name__ == "__main__":
    unittest.main()
