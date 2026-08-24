#include "raylib.h"
#include <random>
#include <string>

using namespace std;


// 随机数生成
int RandomNumber(int min, int max)
{
    static random_device rd;
    static mt19937 gen(rd());

    uniform_int_distribution<int> dis(min, max);

    return dis(gen);
}


int main()
{
    const int WIDTH = 800;
    const int HEIGHT = 450;

    InitWindow(WIDTH, HEIGHT, "Raylib Guess Number Game");

    SetTargetFPS(60);


    // 游戏参数
    int minNum = 1;
    int maxNum = 100;

    int answer = RandomNumber(minNum, maxNum);

    int maxTry = 7;
    int currentTry = 0;


    string input = "";
    string message = "Guess a number (1-100)";

    int score = 0;

    bool gameOver = false;


    Rectangle button = {
        550, 230,
        150, 50
    };


    while (!WindowShouldClose())
    {

        // 键盘输入数字
        int key = GetCharPressed();

        while (key > 0)
        {
            if (key >= '0' && key <= '9')
            {
                input += (char)key;
            }

            key = GetCharPressed();
        }


        // 删除
        if (IsKeyPressed(KEY_BACKSPACE))
        {
            if (!input.empty())
                input.pop_back();
        }


        // 点击猜测按钮
        if (CheckCollisionPointRec(GetMousePosition(), button)
            && IsMouseButtonPressed(MOUSE_BUTTON_LEFT))
        {

            if (!input.empty() && !gameOver)
            {
                int guess = stoi(input);

                currentTry++;


                if (guess == answer)
                {
                    score = (maxTry - currentTry + 1) * 100;

                    message =
                        "Correct! Reward: "
                        + to_string(score);

                    gameOver = true;
                }

                else if (guess < answer)
                {
                    message = "Too small!";
                }

                else
                {
                    message = "Too big!";
                }


                if (currentTry >= maxTry && !gameOver)
                {
                    message =
                        "Game Over! Answer: "
                        + to_string(answer);

                    gameOver = true;
                }


                input = "";
            }
        }


        BeginDrawing();

        ClearBackground(RAYWHITE);


        DrawText(
            "Guess Number Game",
            230,
            40,
            40,
            DARKBLUE
        );


        DrawText(
            message.c_str(),
            180,
            120,
            30,
            BLACK
        );


        // 输入框
        DrawRectangle(
            250,
            180,
            300,
            50,
            LIGHTGRAY
        );


        DrawText(
            input.c_str(),
            270,
            190,
            35,
            BLACK
        );


        // 按钮
        DrawRectangleRec(
            button,
            BLUE
        );


        DrawText(
            "GUESS",
            580,
            240,
            25,
            WHITE
        );


        // 次数
        string times =
            "Try: "
            + to_string(currentTry)
            + "/"
            + to_string(maxTry);


        DrawText(
            times.c_str(),
            320,
            300,
            25,
            DARKGRAY
        );


        EndDrawing();

    }


    CloseWindow();

    return 0;
}