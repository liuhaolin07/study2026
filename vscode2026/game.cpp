#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <limits>
#include <windows.h>
#include <string>
#include <vector>

struct Student {
    std::string name;
    int hp;
    int maxHp;
    int atk;
    int skill;
    std::vector<std::string> sprite;
};

int rng(int l, int r) {
    return l + std::rand() % (r - l + 1);
}

std::string hpBar(int hp, int maxHp, int width = 20) {
    int fill = (maxHp == 0) ? 0 : hp * width / maxHp;
    fill = std::clamp(fill, 0, width);
    return "[" + std::string(fill, '#') + std::string(width - fill, '-') + "]";
}

void clearScreen() {
    std::cout << "\x1B[2J\x1B[H";
}

void sleepMs(int ms) {
    Sleep(static_cast<DWORD>(ms));
}

void drawBattleScene(const Student &shiroko, const Student &hoshino, const Student &enemy, int turn, const std::string &log) {
    clearScreen();
    std::cout << "=== 蔚蓝档案风格战斗可视化（终端版）===\n";
    std::cout << "回合: " << turn << "\n\n";

    std::cout << "敌方: " << enemy.name << "  HP " << enemy.hp << "/" << enemy.maxHp << " " << hpBar(enemy.hp, enemy.maxHp) << "\n";
    for (const auto &line : enemy.sprite) std::cout << "    " << line << "\n";

    std::cout << "\n-----------------------------------------------\n\n";

    std::cout << "我方1: " << shiroko.name << " HP " << shiroko.hp << "/" << shiroko.maxHp << " " << hpBar(shiroko.hp, shiroko.maxHp) << "\n";
    for (const auto &line : shiroko.sprite) std::cout << "    " << line << "\n";

    std::cout << "\n我方2: " << hoshino.name << " HP " << hoshino.hp << "/" << hoshino.maxHp << " " << hpBar(hoshino.hp, hoshino.maxHp) << "\n";
    for (const auto &line : hoshino.sprite) std::cout << "    " << line << "\n";

    std::cout << "\n[战斗日志] " << log << "\n";
}

int readChoice() {
    int choice;
    while (true) {
        std::cin >> choice;
        if (!std::cin.fail() && (choice == 1 || choice == 2)) {
            return choice;
        }
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "输入无效，请输入 1 或 2: ";
    }
}

int main() {
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    Student shiroko{"白子", 120, 120, 18, 35, {" /\\_/\\ ", "( o.o )", " > ^ < "}};
    Student hoshino{"星野", 160, 160, 14, 28, {"  .--.  ", " (o_o ) ", " /|_|\\ "}};
    Student enemy{"凯撒PMC队长", 260, 260, 16, 30, {" [####] ", " /|==|\\", " /_||_\\"}};

    std::vector<Student*> team = {&shiroko, &hoshino};
    int turn = 1;
    std::string log = "战斗开始！";

    while (enemy.hp > 0 && (shiroko.hp > 0 || hoshino.hp > 0)) {
        drawBattleScene(shiroko, hoshino, enemy, turn, log);

        for (Student *s : team) {
            if (s->hp <= 0 || enemy.hp <= 0) continue;

            drawBattleScene(shiroko, hoshino, enemy, turn, s->name + " 准备行动");
            std::cout << "\n轮到 " << s->name << "：1) 普通攻击  2) EX技能\n";
            std::cout << "请输入指令: ";
            int choice = readChoice();

            int dmg = 0;
            if (choice == 2) {
                dmg = std::max(1, s->skill + rng(-4, 6));
                log = s->name + " 使用 EX 技能，造成 " + std::to_string(dmg) + " 点伤害！";
            } else {
                dmg = std::max(1, s->atk + rng(-3, 3));
                log = s->name + " 普攻命中，造成 " + std::to_string(dmg) + " 点伤害。";
            }

            enemy.hp = std::max(0, enemy.hp - dmg);
            drawBattleScene(shiroko, hoshino, enemy, turn, log);
            sleepMs(550);
        }

        if (enemy.hp <= 0) break;

        std::vector<Student*> alive;
        for (Student *s : team) {
            if (s->hp > 0) alive.push_back(s);
        }
        if (alive.empty()) break;

        Student *target = alive[rng(0, static_cast<int>(alive.size()) - 1)];
        int enemyDamage;
        if (rng(1, 100) <= 25) {
            enemyDamage = enemy.skill + rng(0, 8);
            log = "敌方发动重火力压制！";
        } else {
            enemyDamage = enemy.atk + rng(-2, 5);
            log = "敌方发动攻击。";
        }

        drawBattleScene(shiroko, hoshino, enemy, turn, log);
        sleepMs(450);

        enemyDamage = std::max(1, enemyDamage);
        target->hp = std::max(0, target->hp - enemyDamage);
        log = target->name + " 受到 " + std::to_string(enemyDamage) + " 点伤害。";
        drawBattleScene(shiroko, hoshino, enemy, turn, log);
        sleepMs(550);

        turn++;
    }

    if (enemy.hp <= 0) {
        log = "任务成功！老师带领大家守住了据点。";
    } else {
        log = "任务失败……请重新编队再战。";
    }
    drawBattleScene(shiroko, hoshino, enemy, turn, log);
    std::cout << "\n战斗结束，按回车退出。";
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cin.get();

    return 0;
}