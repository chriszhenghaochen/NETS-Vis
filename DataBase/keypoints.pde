PImage img;
String text = "";
float x = 0;
float y = 0;

void setup() {
  size(1000,1000);
  img = loadImage("U:\\ho\\input.jpg");
}

void draw() {
  image(img, 0, 0, 1000, 1000);
  textSize(32);
  text(text, 10,30);
  //text(text, x, y);
 
}

void mouseClicked() {
   if(mouseButton == RIGHT){
     print(mouseX + ","+ mouseY);
     print("\n");
     x = mouseX;
     y = mouseY;
     text = mouseX + ","+ mouseY;
   }
}