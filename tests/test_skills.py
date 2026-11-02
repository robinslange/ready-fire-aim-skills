"""Every skill loads: frontmatter has a name matching its folder and a
"Use when" description inside the length limit, and every skill a skill
points to exists."""
import os, re, unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(REPO, "skills")
NAMES = sorted(os.listdir(SKILLS))


def frontmatter(name):
    with open(os.path.join(SKILLS, name, "SKILL.md")) as f:
        text = f.read()
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    assert m, f"{name}: no frontmatter"
    fields = dict(line.split(": ", 1) for line in m.group(1).splitlines())
    return fields, m.group(2)


class SkillsTest(unittest.TestCase):
    def test_frontmatter(self):
        for name in NAMES:
            fields, _ = frontmatter(name)
            self.assertEqual(fields["name"], name)
            self.assertTrue(fields["description"].startswith("Use when"), name)
            self.assertLessEqual(len(fields["description"]), 1024, name)

    def test_cross_references_resolve(self):
        for name in NAMES:
            _, body = frontmatter(name)
            for ref in re.findall(r"`([a-z]+(?:-[a-z]+)+)`", body):
                self.assertIn(ref, NAMES, f"{name} points to missing skill {ref}")


if __name__ == "__main__":
    unittest.main()
