"I'm a module documentation"

# __name__
import settings

print(f"{settings.app_name}/{settings.app_version}")
print(f"Module name (__name__): {__name__}")
print(f"{__doc__=}, {__package__=}, {__spec__=}")

def main():
    print("I'm a main finction!")

if __name__ == "__main__":
    print("I'm running as a script!")
    main()
