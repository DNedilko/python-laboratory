#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <conio.h>
#include <time.h>
#include <locale.h>
#include <Windows.h>

void position(int x, int y) {
    COORD position;
    position.X = x;
    position.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), position);
}

void frame(){
    position(19,0);puts("\311");
    for (int x=20; x<=60; x++){
        position(x, 0);
        printf("\315");
    }
    position(61,0);puts("\273");
    for (int y=1; y<=11; y++){
        position(19, y);
        printf("\272");
    }
    for (int y=1; y<=11; y++){
        position(61, y);
        printf("\272");
    }
    position(19,12);puts("\310");
    for (int x=20; x<=60; x++){
        position(x, 12);
        printf("\315");
    }
    position(61,12);puts("\274");

    setlocale(LC_ALL, "Rus");

    position(30,2);puts("Labarotory №1");
    position(21,4);puts("\"Базовi типи даних, уведення-виведення,");
    position(23,5);puts("бiтовi операцiї, операцiї зсуву\"");
    position(21,7);puts("Виконала студентка групи КМ-91");
    position(21,8);puts("Гудим Вiкторiя");
    position(49,9);puts("Громова В.В.");
    position(38,11);puts("2020");
}

int valid_int(){
    int num;
    char term;
    while (!scanf("%d%c", &num, &term) || term != '\n')
    {
        rewind(stdin);
        printf("--- Помилка типу даних. Спробуйте знову: ");
        fflush(stdin);
    }
    return num;
}

float valid_float(){
    float number;
    char term;
    while (!scanf("%f%c", &number, &term) || term != '\n')
    {
        rewind(stdin);
        printf("--- Помилка типу даних. Спробуйте знову: ");
        fflush(stdin);
    }
    return number;
}

int valid_hex(){
    int UnitStateWord;
    while (!scanf("%x", &UnitStateWord))
    {
        rewind(stdin);
        printf("--- Помилка типу даних. Спробуйте знову: ");
        fflush(stdin);
    }
    return UnitStateWord;
}

char getdata(){
    char ch;
    while(1){
        printf("\nВиберiть один iз варiантiв:\n  1.Ввести данi самостiйно\n  2.Згенерувати числа\n");
        ch = getch();
        if (ch == '1' || ch == '2')
            break;
        printf("--- Некоректнi символи. Спробуйте знову: ");
    }
    return ch;
}


void first_task(){
    system("cls");
    char ch;
    float a, b, result;
    ch = getdata();
    switch(ch){
        case '1':
            printf("\nВведiть число a: ");
            a = valid_float();
            printf("Введiть число b: ");
            b = valid_float();
            break;
        case '2':
            a = -20 + rand() %20;
            b = -20 + rand() %20;
            printf("\nЗгенерованi числа: a = %.2f, b = %.2f", a, b);
            break;
    }
    result = pow((a + b),3);
    printf("\nРезультат: (%.3f+%.3f)^3 = %.2f\n", a, b, result);
}

void second_task(){
    system("cls");
    char ch;
    float density, residents, square;
    ch = getdata();
    switch(ch){
        case '1':
            printf("\nКiлькiсть жителiв (осiб): ");
            residents = valid_int();
            if (residents<=0){
                do {
                    printf("---Ця величина не може бути вiд'ємною! Спробуйте ще: ");
                    residents = valid_int();
                } while (residents<=0);
            }
            printf("Площа територiї держави (кв.од.): ");
            square = valid_int();
            if (square<=0){
                do {
                    printf("---Ця величина не може бути вiд'ємною! Спробуйте ще: ");
                    square = valid_int();
                } while (square<=0);
            }
            break;
        case '2':
            residents = 1 + rand() %1000;
            square = 1 + rand() %1000;
            printf("\nЗгенерованi данi: к-сть жителiв = %.f, площа = %.f\n", residents, square);
            break;
    }

    density = residents/square;
    printf("\nЩiльнiсть населення становить %.2f осiб/кв.од.\n", density);
}

void third_task()
{
    system("cls");
    int P, F, H, V;
    unsigned int UnitStateWord;
    printf("\nВведiть кiлькiсть принтерiв P (0-7): ");
    P = valid_int();
    while ((P > 7) | (P < 0)){
        printf("--- Не правильне значення. Спробуйте ще: ");
        P = valid_int();
    }
    printf("Введiть кiлькiсть гнучких дискiв F (0-3): ");
    F = valid_int();
    while ((F < 0) | (F > 3)){
        printf("--- Не правильне значення. Спробуйте ще: ");
        F = valid_int();
    }
    printf("Введiть тип жорсткого диску H (0-15): ");
    H = valid_int();
    while ((H < 0) | (H > 15)){
        printf("--- Не правильне значення. Спробуйте ще: ");
        H = valid_int();
    }
    printf("Введiть тип вiдеоадаптера V (0-7): ");
    V = valid_int();
    while ((V < 0) | (V > 7)){
        printf("--- Не правильне значення. Спробуйте ще: ");
        V = valid_int();
    }
    UnitStateWord = ((unsigned int)P & 7) << 13;
    UnitStateWord |= ((unsigned int)F & 0x3) << 10;
    UnitStateWord |= ((unsigned int)H & 0xF) << 5;
    UnitStateWord |= V & 0x7;
    printf("\nСлово стану пристрою = %04x\n", UnitStateWord);
}

void fourth_task(){
    system("cls");
    char P, F, H, V;
    unsigned int UnitStateWord;
    printf("\nВведiть слово стану пристрою \n(шiстнадцяткове число вiд 0 до 0хFFFF): ");
    UnitStateWord = valid_hex();
    P = (UnitStateWord >> 13) & 7;
    F = (UnitStateWord >> 10) & 0x3;
    H = (UnitStateWord >> 5) & 0xF;
    V = UnitStateWord & 0x7;

    printf("\nКількiсть принтерiв  = %d\n", P);
    printf("Кiлькiсть гнучких дискiв = %d\n", F);
    printf("Тип жорсткого диску = %d\n", H);
    printf("Тип вiдеоадаптера = %d\n", V);
    fflush(stdin);
}


int main(){
    frame();
    setlocale(LC_ALL, "Rus");
    int task;
    char answer;
    do{
        printf("\nОберiть номер завдання (1-4):\n  1.Обчислення кубу суми\n  2.Щiльнiсть населення\n  3.Упакування\n  4.Розпакування\n");
        task = valid_int();
        if (task == 1) {
            first_task();
        }
        else if (task == 2){
            second_task();
        }
        else if (task == 3){
            third_task();
        }
        else if (task == 4){
            fourth_task();
        }
        else{
            printf("--- Такого номеру не iснує!\n");
        }
        printf("\n--- Натиснiть 1, щоб продовжити, або будь-який iнший символ, щоб завершити ---\n");
        scanf("%c", &answer);
        system("cls");

    } while (answer == '1');
}
//
// Created by Meduzka on 19/02/2020.
//

