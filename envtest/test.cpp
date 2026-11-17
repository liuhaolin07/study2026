#include <iostream>
#ifdef _WIN32
#include <windows.h>
#endif

using namespace std;

int main()
{
    int a;
    cin >> a;

#ifdef _WIN32
    HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_SCREEN_BUFFER_INFO info;
    WORD originalAttributes = 0;
    if (GetConsoleScreenBufferInfo(console, &info)) {
        originalAttributes = info.wAttributes;
        SetConsoleTextAttribute(console, FOREGROUND_RED | FOREGROUND_GREEN |
                                           FOREGROUND_BLUE | FOREGROUND_INTENSITY);
    }
#endif

    cout << "+----------------------------------+" << endl;
    cout << "| Hello, World!                    |" << endl;
    cout << "| The value of a is: " << a << "             |" << endl;
    cout << "+----------------------------------+" << endl;

#ifdef _WIN32
    if (originalAttributes != 0) {
        SetConsoleTextAttribute(console, originalAttributes);
    }
#endif

    return 0;
}