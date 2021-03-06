PShape s, init, target;
float a;
ArrayList<PVector> init_verts, target_verts;
boolean toggle;
PVector coords;

void setup() {
  size(500, 500);
  background(255);
  blendMode(DIFFERENCE);
  s = loadShape("TriCircSmooth.svg");
  frameRate(30);

  init_verts = new ArrayList<PVector>();
  target_verts = new ArrayList<PVector>();

  for (int i = 0; i < s.getChild(0).getVertexCount(); i++) {
    init_verts.add(s.getChild(0).getVertex(i).copy());
  }
  for (int i = 0; i < s.getChild(1).getVertexCount(); i++) {
    target_verts.add(s.getChild(1).getVertex(i).copy());
  }

  coords=new PVector(375,334); //284, 252

}

void draw() {
  background(255);
  scale(0.25);
  for (int i = -1; i < 30; i++) {
    for (int j = -1; j < 30; j++) {
      float param = 8.0*(i+j)/(82);
      if (j % 2 == 0) {
        func(coords.x*i, coords.y*j, param);
      } else {
        func(coords.x*i-coords.x/2, coords.y*j, param);
      }
    }
  }

  //saveFrame("animation/output####.jpg");
  if (mousePressed) println(mouseX, mouseY);
}

void mousePressed() {
  coords = new PVector(mouseX, mouseY);
}

void func(float x, float y, float param) {
  for (int i = 0; i < s.getChild(0).getVertexCount(); i++) {
    PVector v_init = init_verts.get(i);
    PVector v_target;
    v_target = target_verts.get(i);

    PVector mix = PVector.lerp(v_init, v_target, 2.6*sin(0.044*a+param+PI));

    s.getChild(0).setVertex(i, mix);
  }


  s.disableStyle();
  pushStyle();
  fill(255);
  stroke(0);
  strokeWeight(2);

  PShape curve = s.getChild(0);
  shape(curve, x, y);

  popStyle();

  a+=0.001;
}
