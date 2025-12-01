#include <fstream>
#include <iostream>
#include <string>

int main() {
    std::ifstream inputFile("input.txt");
    if (!inputFile.is_open()) {
        std::cout << "Error opening file." << std::endl;
        return 1;
    }

    int num_zeros_pt1 = 0;
    int num_zeros_pt2 = 0;

    int current_rotation_pt1 = 50;
    int current_rotation_pt2 = 50;

    std::string line;
    std::string direction;
    int num_steps;
    while (std::getline(inputFile, line)) {
        direction = line.substr(0, 1);
        num_steps = std::stoi(line.substr(1));

        std::cout << "Direction: " << direction << ", Steps: " << num_steps
                  << std::endl;

        current_rotation_pt1 =
            (direction == "R") ? (current_rotation_pt1 + num_steps) % 100
                               : (current_rotation_pt2 - num_steps + 100) % 100;

        if (current_rotation_pt1 == 0)
            num_zeros_pt1++;

        int increment = (direction == "R") ? 1 : -1;
        for (int i = 0; i < num_steps; i++) {
            current_rotation_pt2 =
                (current_rotation_pt2 + increment + 100) % 100;
            if (current_rotation_pt2 == 0)
                num_zeros_pt2++;
        }
    }

    std::cout << "Part 1: " << num_zeros_pt1 << std::endl;
    std::cout << "Part 2: " << num_zeros_pt2 << std::endl;

    inputFile.close();
    return 0;
}