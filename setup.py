from cx_Freeze import setup, Executable


setup(
    name = "townstar",
    version = "0.1",
    description = "",
    executables = [Executable("townstar.py")]
)
