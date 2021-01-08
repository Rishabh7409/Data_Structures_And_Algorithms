
// Definition for Graph Edge Class
/** 
Graph_Edge(int src, int dest, int wght){
        this.source=src;
        this.destination=dest;
        this.weight=wght;
    }
 */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Graph_BFS_Traversal {
    
    // hashmap to store graph in form of adjacency list 
    HashMap<Integer,ArrayList<Graph_Edge>> graph=new HashMap<>(); 
    ArrayList<Character> vertices;

    // constructor
    Graph_BFS_Traversal(ArrayList<Character> arr){
        this.vertices=arr;

    }
    
    // Undirected Edge
    void add_Non_Directed_Edge(int src,int dest,int weight){
        
        // Create Two Nodes
        Graph_Edge edge1=new Graph_Edge(src,dest,weight);
        Graph_Edge edge2=new Graph_Edge(dest,src,weight);
        ArrayList<Graph_Edge> ar1;
        ArrayList<Graph_Edge> ar2;

        // if the source node is already present
        if(this.graph.containsKey(src)){
            ar1=this.graph.get(src);
            ar1.add(edge1);
            graph.put(src,ar1);
        }

        else {
            ar1=new ArrayList<>();
            ar1.add(edge1);
            graph.put(src,ar1);
        }

        // if destination node is already present
        if(this.graph.containsKey(dest)){
            ar2=this.graph.get(dest);
            ar2.add(edge2);
            graph.put(dest,ar2);
        }
        else {
            ar2=new ArrayList<>();
            ar2.add(edge2);
            graph.put(dest,ar2);
        }

    }

    // Function For Adding Directed Edge
    void add_Directed_Edge(int src,int dest,int weight){

        Graph_Edge edge=new Graph_Edge(src,dest,weight);
        ArrayList<Graph_Edge> ar;
        if(this.graph.containsKey(src)){
            ar=this.graph.get(src);
            ar.add(edge);
        }
        else {
            ar=new ArrayList<>();
            ar.add(edge);
            this.graph.put(src,ar);
        }
        // create an empty place for destination node
        this.graph.put(dest,new ArrayList<>());
    }

    // Adjcency List Representation
    void Adjacency_List(){
        for(Map.Entry<Integer,ArrayList<Graph_Edge>> itr:this.graph.entrySet()){
            System.out.print(this.vertices.get(itr.getKey())+" : ");
            for(Graph_Edge ed:itr.getValue()){
                System.out.print(this.vertices.get(ed.destination)+" ");
            }
            System.out.println();
        }
    }

    // Breadth First Search In Graph Using Queue
    void BFS_Traversal(){
        ArrayList<Integer> ar=new ArrayList<>(); //Queue to store vertices
        ArrayList<Character> bfs=new ArrayList<>();
        ar.add(0);
        while (!(ar.size()==0)){
            int x=ar.remove(0);
            bfs.add(this.vertices.get(x));
            for(Graph_Edge ed:this.graph.get(x)){
                if(!bfs.contains(this.vertices.get(ed.destination))&&(!ar.contains(ed.destination))){
                    ar.add(ed.destination);
                }
            }
        }
        System.out.print("The BFS Traversal of The Graph Is : "+bfs);

    }

    public static void main(String[] args) {

        Scanner scan=new Scanner(System.in);
        ArrayList<Character> characterArray=new ArrayList<>();
        
        int x=6;
        for(int i=0;i<x;i++){
            //You can give vertices names as input
            System.out.print("Enter "+i+" Vertex : ");
            characterArray.add(scan.next().charAt(0));
        }

        scan.close();

        Graph_BFS_Traversal gr=new Graph_BFS_Traversal(characterArray);
        gr.add_Non_Directed_Edge(0,1,0);  //(source, destination,weight)
        gr.add_Directed_Edge(0,5,0);
        gr.add_Non_Directed_Edge(1,3,0);
        gr.add_Directed_Edge(3,4,0);
        gr.add_Directed_Edge(4,2,0);
        gr.add_Non_Directed_Edge(5,1,0);
        gr.add_Non_Directed_Edge(1,2,0);

        gr.Adjacency_List();
        gr.BFS_Traversal();
    }
}
