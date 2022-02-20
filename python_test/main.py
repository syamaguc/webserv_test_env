import sys
from test_get import test_get
from test_post import test_post
from test_delete import test_delete
from test_other import test_other


if __name__ == "__main__":
    if (sys.argv[1] == "get"):
        test_get()
    elif (sys.argv[1] == "post"):
        test_post()
    elif (sys.argv[1] == "delete"):
        test_delete()
    elif (sys.argv[1] == "other"):
        test_other()
    else:
        pass
