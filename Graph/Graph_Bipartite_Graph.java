/**
 In this program we wil check that if the graph is bipartite graph
  
 Bipartite Graph:
    * A Bipartite Graph is a graph whose vertices can be divided into two independent sets, U and V such that every edge (u, v) either connects a vertex from U to V or a vertex from V to U. In other words, for every edge (u, v), either u belongs to U and v to V, or u belongs to V and v to U. We can also say that there is no edge that connects vertices of same set.
    */


 //It is A 2-coloring Graph Problem

 // in This Program We Have Used Undirected Graph  


// Definition for Graph Edge Class
/** 
Graph_Edge(int src, int dest, int wght){
        this.source=src;
        this.destination=dest;
        this.weight=wght;
    }
 */




import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
public class Graph_Bipartite_Graph{

    ArrayList<Character> Vertices;
    HashMap<Integer,ArrayList<Graph_Edge>> graph=new HashMap<>();

    Graph_Bipartite_Graph(ArrayList<Character> vert){
        this.Vertices=vert;
    }

    // Undirected Edge
    private void Add_Edge(int src,int dest,int weight)
    {
        Graph_Edge edge=new Graph_Edge(src,dest,weight);
        if(this.graph.containsKey(src)){
            this.graph.get(src).add(edge);
        }
        else{
            ArrayList<Graph_Edge> ar=new ArrayList<>();
            ar.add(edge);
            this.graph.put(src,ar);
        }

        Graph_Edge edge2=new Graph_Edge(dest,src,weight);
        if(this.graph.containsKey(dest)){
            this.graph.get(dest).add(edge2);
        }
        else{
            ArrayList<Graph_Edge> ar=new ArrayList<>();
            ar.add(edge2);
            this.graph.put(dest,ar);
        }

        
    }


    private boolean IsBipartite(){

        //we will use 0 and 1 as colors
        int current_color=0;  

        // color array for each edge
        int []color=new int[this.Vertices.size()];
        Arrays.fill(color, -1);
        for(HashMap.Entry<Integer,ArrayList<Graph_Edge>> itr:this.graph.entrySet()){

            int curr_key=itr.getKey();
            // if current vertex is not colored
            if(color[curr_key]==-1){
                color[curr_key]=current_color;
            }

            // change the color because no two nodes can have same color
            current_color=1-color[curr_key];

            for(Graph_Edge ed:itr.getValue()){

                // if any adjacent node is already colored then return false

                if(color[ed.destination]==color[curr_key]){

                    return false;
                }
                // if the node is not colored then color it
                else if(color[ed.destination]==-1){

                    color[ed.destination]=current_color;
                }
            }
        }

        // color of each node
        // System.out.print("\nColors: ");
        // for(int x:color){
        //     System.out.print(x+" ");
        // }

        return true; //since all the vertices are colored with different color
    }

    private void Display_Graph(HashMap<Integer,ArrayList<Graph_Edge>> graph){
        for(HashMap.Entry<Integer,ArrayList<Graph_Edge>> itr:graph.entrySet()){
            System.out.print(itr.getKey()+" : ");
            for(Graph_Edge ed:itr.getValue()){
                System.out.print(ed.destination+" ");
            }
            System.out.println();
        }
    }


    public static void main(String[] args) {

        ArrayList<Character> vert=new ArrayList<>();
        vert.add('A');
        vert.add('B');
        vert.add('C');
        vert.add('D');
        vert.add('E');
        vert.add('F');
        vert.add('G');
        vert.add('H');
        Graph_Bipartite_Graph object=new Graph_Bipartite_Graph(vert);

        // Create Graph
        object.Add_Edge(0,1,0);
        object.Add_Edge(0,2,0);
        object.Add_Edge(0,4,0);
        object.Add_Edge(1,3,0);
        object.Add_Edge(1,5,0);
        object.Add_Edge(2,3,0);
        object.Add_Edge(2,6,0);
        object.Add_Edge(3,7,0);
        object.Add_Edge(4,5,0);
        object.Add_Edge(4,6,0);
        object.Add_Edge(5,7,0);

        
        object.Display_Graph(object.graph);
        boolean val=object.IsBipartite();
        System.out.println(val?"\n\nThis Is Bipartite Graph\n":"\nThis Is Not A Bipartite Graph\n");
    }

}