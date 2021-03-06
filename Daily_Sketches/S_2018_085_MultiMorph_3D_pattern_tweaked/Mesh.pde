import java.util.*;

class Mesh {
  PShape obj;
  ArrayList<PVector> vertices;
  ArrayList<int[]> faces;

  Mesh(PShape obj) {
    this.obj = obj;
    this.vertices = new ArrayList<PVector>();
    this.faces = new ArrayList<int[]>();

    //Add all vertices to arraylist
    for (int i = 0; i < obj.getChildCount(); i++) {
      for (int j = 0; j < obj.getChild(i).getVertexCount(); j++) {
        PVector vec = obj.getChild(i).getVertex(j);
        this.vertices.add(vec);
      }
    }

    //Remove duplicates from ArrayList;
    this.vertices = new ArrayList<PVector>(new LinkedHashSet(vertices));

    //Add all faces to arraylist
    for (int i = 0; i < obj.getChildCount(); i++) {
      int[] faceindex = new int[obj.getChild(i).getVertexCount()];
      for (int j = 0; j < obj.getChild(i).getVertexCount(); j++) {
        PVector vec = obj.getChild(i).getVertex(j);
        faceindex[j]=vertices.indexOf(vec);
      }
      faces.add(faceindex);
    }
  }

  void morph(Mesh initial, Mesh target, float a) {
    //Morphs between initial and target mesh
    for (int i = 0; i < this.vertices.size(); i++) {
      float param = 0.0 * i/this.vertices.size();
      PVector vec = PVector.lerp(initial.vertices.get(i), 
                          target.vertices.get(i), 
                          map(cs(a+param), -1, 1, 0, 1));
      this.vertices.set(i, vec);
    }
    
  }

  void shuffle() {
    //Randomly shuffles vertices
    for (int i = 0; i < this.vertices.size(); i++) {
      PVector vec = this.vertices.get(i).mult(random(0.9, 1.1));
      this.vertices.set(i, vec);
    }
  }


  void display(float a) {
    pushStyle();
    noFill();
    stroke(0,25);
    fill(235, 0, 120);
    strokeWeight(0.1);
    noStroke();
    beginShape(QUADS);
    for (int i = 0; i < faces.size(); i++) {
      float param1 = 1.0 *i/faces.size();

      for (int j = 0; j < faces.get(i).length; j++) {
        float param2 = 0.0 * i/faces.get(i).length;
        fill(lerpColor(#ffe400, #212121, map(cs(a+param1+param2), -1, 1, 0, 1)));  
        //ffe400,0EC0E1,DD3A7C,1a1a1a
        int index = faces.get(i)[j];
        PVector vec = this.vertices.get(index);
        vertex(vec.x, vec.y, vec.z);
      }
    }
    endShape();
    popStyle();
  }
}
