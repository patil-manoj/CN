#include <iostream>
#include <string.h>

using namespace std;

int crc(char *ip, char *op, char *poly, int mode)
{
    strcpy(op, ip);

    // Append 0's to the dividend
    if (mode)
    {
        for (int i = 1; i < strlen(poly); i++)
        {
            strcat(op, "0");
        }
    }

    // Perform XOR on the msg with the selected polynomial
    for (int i = 0; i < strlen(ip); i++)
    {
        if (op[i] == '1')
        {
            for (int j = 0; j < strlen(poly); j++)
            {
                if (op[i + j] == poly[j])
                {
                    op[i + j] = '0';
                }
                else
                {
                    op[i + j] = '1';
                }
            }
        }
    }

    // Check for errors
    if (!mode)
    {
        for (int i = 0; i < strlen(op); i++)
        {
            if (op[i] == '1')
            {
                return 0;
            }
        }
        return 1;
    }
}

int main(void)
{
    char ip[50], op[50], recv[50];
    char poly[] = "10001000000100001";

    // Sender's side
    cout << "Enter the input message in binary: ";
    cin >> ip;

    crc(ip, op, poly, 1);

    cout << "The transmitted message is: " << ip << op + strlen(ip) << endl;

    // Receiver's side
    cout << "Enter the recevied message in binary: ";
    cin >> recv;

    if (crc(recv, op, poly, 0))
    {
        cout << "No error in data" << endl;
    }
    else
    {
        cout << "Error in data transmission!" << endl;
    }
}