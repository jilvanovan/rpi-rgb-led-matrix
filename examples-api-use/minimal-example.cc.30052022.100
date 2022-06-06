// -*- mode: c++; c-basic-offset: 2; indent-tabs-mode: nil; -*-
// Small example how to use the library.
// For more examples, look at demo-main.cc
//
// This code is public domain
// (but note, that the led-matrix library this depends on is GPL v2)

#include "led-matrix.h"
#include "graphics.h"

#include <iostream>
#include <fstream>
#include <string>
using namespace std;



#include <unistd.h>
#include <math.h>
#include <stdio.h>
#include <signal.h>

#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// using rgb_matrix::RGBMatrix;
// using rgb_matrix::Canvas;

using namespace rgb_matrix;

volatile bool interrupt_received = false;
static void InterruptHandler(int signo) {
  interrupt_received = true;
}

static bool parseColor(Color *c, const char *str) {
  return sscanf(str, "%hhu,%hhu,%hhu", &c->r, &c->g, &c->b) == 3;
}

static bool FullSaturation(const Color &c) {
  return (c.r == 0 || c.r == 255)
    && (c.g == 0 || c.g == 255)
    && (c.b == 0 || c.b == 255);
}

static void DrawOnCanvas(Canvas *canvas) {
  /*
   * Let's create a simple animation. We use the canvas to draw
   * pixels. We wait between each step to have a slower animation.
   */

  // canvas->Fill(255, 255, 255);
  // sleep(1);
  // canvas->Fill(255, 0, 0);
  // sleep(1);
  // canvas->Fill(0, 255, 0);
  // sleep(1);
  // canvas->Fill(0, 0, 255);
  // sleep(1);

  rgb_matrix::Font font;
  printf("Loading Font\n");
  if (!font.LoadFont("../fonts/arial.bdf")) {
    fprintf(stderr, "Couldn't load font '%s'\n", "error");
  }

  Color color(0, 255, 0);
  Color bg_color(0, 0, 0);
  Color flood_color(0, 0, 0);
  Color outline_color(0,0,0);
  canvas->Fill(flood_color.r, flood_color.g, flood_color.b);
  bool with_outline = false;

  // const char *bdf_font_file = NULL;
  int x_orig = 5;
  int y_orig = -6;
  int letter_spacing = 2;

  rgb_matrix::Font *outline_font = NULL;
  if (with_outline) {
    outline_font = font.CreateOutlineFont();
  }

  const int x = x_orig;
  int y = y_orig;
  char line[1024];
  while(1){
  string sbuff;
  ifstream myfile ("/home/pi/perpython/example.json");
  if (myfile.is_open())
  {
    while ( getline (myfile,sbuff) )
    {
      cout << sbuff << '\n';
    }
    myfile.close();
  }

  if (sbuff=="0"){
      canvas->Fill(0, 0, 0);
  }
    char clientid[25];
    char imbuffer[1];
      rgb_matrix::DrawText(canvas, font, x, y + font.baseline(),
                         color, outline_font ? NULL : &bg_color, sbuff.c_str(),
                         letter_spacing-2);
    sleep(1);
  }
    
}

int main(int argc, char *argv[]) {
  RGBMatrix::Options defaults;
  RuntimeOptions defaults2;
  defaults.hardware_mapping = "adafruit-hat";  // or e.g. "adafruit-hat"
  defaults.rows = 16;
  defaults.cols = 32;
  defaults.chain_length = 4;
  defaults.parallel = 1;
  // defaults.show_refresh_rate = true;
  defaults.brightness = 10;
  defaults.multiplexing=11;
  defaults.led_rgb_sequence="BGR";
  defaults.row_address_type=0;
  defaults2.gpio_slowdown=5;
  Canvas *canvas = RGBMatrix::CreateFromFlags(&argc, &argv, &defaults);
  if (canvas == NULL)
    return 1;

  // It is always good to set up a signal handler to cleanly exit when we
  // receive a CTRL-C for instance. The DrawOnCanvas() routine is looking
  // for that.
  signal(SIGTERM, InterruptHandler);
  signal(SIGINT, InterruptHandler);

  DrawOnCanvas(canvas);    // Using the canvas.
  sleep(1);
  // Animation finished. Shut down the RGB matrix.
  canvas->Clear();
  delete canvas;

  return 0;
}
