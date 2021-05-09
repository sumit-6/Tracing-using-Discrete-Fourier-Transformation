let y1 = [];
let x1 = [];
let fourierY_1;
let fourierX_1;
let time_1 = 0;
let drawing_1=[];

function setup()
{
  createCanvas(1500, 700);
  let max1 = path.length;
  const skip1 = 1;
  for (let i = 0; i<max1; i+=skip1)
  {
      x1.push(path[i].x);
      y1.push(path[i].y);
  }
  fourierX_1 = dft(x1);
  fourierY_1 = dft(y1);

  fourierX_1.sort((a,b) => b.amp - a.amp);
  fourierY_1.sort((a,b) => b.amp - a.amp);
}

function epiCycles(x,y,fourier,rotation)
{
    for (let i = 0; i < fourierY_1.length; i++)
    {
      let prevx = x;
      let prevy = y;
      let freq = fourier[i].freq;
      let radius = fourier[i].amp;
      let phase = fourier[i].phase;
      x += radius*cos((freq * time_1) + phase + rotation);
      y += radius*sin((freq * time_1) + phase + rotation);
      stroke(255,80);
      noFill();
      ellipse(prevx,prevy,radius*2);
    
      fill(255);
      stroke(255,100);
      line(prevx,prevy,x,y);
    }
    return createVector(x,y);
}

function draw() {
    background(0);
  
    let speed = 1;
    
    let vx = epiCycles(width/2,100-40,fourierX_1,0);
    let vy = epiCycles(100,height/2 - 40,fourierY_1,HALF_PI);
    let v = createVector(vx.x,vy.y);
    
    drawing_1.unshift(v);
    stroke(255,90);
    line(vx.x ,vx.y ,v.x,v.y);
    line(vy.x,vy.y,v.x,v.y);
    stroke(255);
    beginShape();
    noFill();
    for (let i = 0;i < drawing_1.length; i++)
    {
      vertex(drawing_1[i].x,drawing_1[i].y);
    }
    endShape();
    const dt = TWO_PI/fourierY_1.length;
    time_1 += (speed*dt);
}