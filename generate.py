import os

MOS_TOPICS = {
    "Unit 1": [
        {"title": "Introduction to Operating Systems", "img": "../images/intro.png", "link": "unit1/intro.html"},
        {"title": "Types of Operating Systems", "img": "../images/types.png", "link": "unit1/types.html"},
        {"title": "Introduction To Linux", "img": "../images/linux.jpg", "link": "unit1/linux.html"},
        {"title": "Basic Linux Commands", "img": "../images/commands.jpg", "link": "unit1/commands.html"},
        {"title": "Inodes and Processes", "img": "../images/inodes.png", "link": "unit1/inodes.html"},
        {"title": "Package Managers", "img": "../images/package.png", "link": "unit1/package.html"},
        {"title": "Memory Management", "img": "../images/memory.jpg", "link": "unit1/memory.html"},
        {"title": "File Systems", "img": "../images/filesystem.png", "link": "unit1/filesystem.html"},
        {"title": "Scheduler", "img": "../images/scheduler.png", "link": "unit1/scheduler.html"},
        {"title": "I/O", "img": "../images/io.jpg", "link": "unit1/io.html"}
    ],
    "Unit 2": [
        {"title": "Shell Scripting", "img": "../images/shell.jpg", "link": "unit2/shell.html"},
        {"title": "Linux Commands for Analytics", "img": "../images/analytics.jpg", "link": "unit2/analytics.html"},
        {"title": "Dialogs", "img": "../images/dialogs.jpg", "link": "unit2/dialogs.html"},
        {"title": "User Management", "img": "../images/user.png", "link": "unit2/user.html"},
        {"title": "Permission Management", "img": "../images/permissions.jpg", "link": "unit2/permissions.html"},
        {"title": "Cron Jobs", "img": "../images/cron.png", "link": "unit2/cron.html"},
        {"title": "SSH", "img": "../images/ssh.png", "link": "unit2/ssh.html"},
        {"title": "Storage", "img": "../images/storage.jpg", "link": "unit2/storage.html"},
        {"title": "Virtualization", "img": "../images/virtualization.jpg", "link": "unit2/virtualization.html"}
    ],
    "Unit 3": [
        {"title": "Interprocess Communication (IPC)", "img": "../images/ipc.jpg", "link": "unit3/ipc.html"},
        {"title": "Distributed Systems", "img": "../images/distributed.png", "link": "unit3/distributed.html"},
        {"title": "Operating System Security", "img": "../images/security.jpg", "link": "unit3/security.html"},
        {"title": "Web Servers", "img": "../images/webserver.jpg", "link": "unit3/webserver.html"},
        {"title": "PXE", "img": "../images/pxe.png", "link": "unit3/pxe.html"},
        {"title": "VNC and RDP", "img": "../images/vnc.jpg", "link": "unit3/vnc.html"},
        {"title": "Linux Containers", "img": "../images/containers.png", "link": "unit3/containers.html"}
    ]
}


# Basic template for each page
PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="../page.css">
</head>
<body>
  <header>
    <h1>{title}</h1>
    <nav>
      <a href="../index.html">Home</a>
    </nav>
  </header>
  <main>
    <section class="content">
    <img src="{img}" alt="{title}" class="topic-image">
      <h2>{title}</h2>
      <p>Notes and explanations for <strong>{title}</strong> will go here.</p>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 | MOS Notes Website | Designed by Srajan</p>
  </footer>
</body>
</html>
"""


def generate_pages():
    for unit, topics in MOS_TOPICS.items():
        unit_folder = unit.lower().replace(" ", "")  # e.g. "Unit 1" -> "unit1"
        os.makedirs(unit_folder, exist_ok=True)

        for topic in topics:
            file_path = topic["link"]
            title = topic["title"]
            img = topic["img"]

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(PAGE_TEMPLATE.format(title=title, img=img))

            print(f"✅ Created: {file_path}")


if __name__ == "__main__":
    generate_pages()
