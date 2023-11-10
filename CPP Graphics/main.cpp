#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <cmath>
#include <algorithm>
using namespace std;

void drawLineDDA(float x1, float y1, float x2, float y2) {
    // Calculate the length of the line
    float dx = x2 - x1;
    float dy = y2 - y1;

    // Find the number of steps to draw the line
    float steps = std::max(std::abs(dx), std::abs(dy));

    // Calculate increments for x and y
    float xIncrement = dx / steps;
    float yIncrement = dy / steps;

    // Starting point of the line
    float x = x1;
    float y = y1;

    // Set the color to white
    glColor3f(1.0, 1.0, 1.0);

    // Draw each pixel along the line using OpenGL
    glBegin(GL_POINTS);
    for (int i = 0; i <= steps; ++i) {
        glVertex2f(x, y);
        x += xIncrement;
        y += yIncrement;
    }
    glEnd();
}

int main() {
    // Initialize GLFW and create a window
    if (!glfwInit()) {
        return -1;
    }

    GLFWwindow* window = glfwCreateWindow(800, 600, "DDA Line Drawing", NULL, NULL);
    if (!window) {
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);

    while (!glfwWindowShouldClose(window)) {
        glClear(GL_COLOR_BUFFER_BIT);

        // Call your DDA line drawing function
        drawLineDDA(100, 100, 500, 400);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}
