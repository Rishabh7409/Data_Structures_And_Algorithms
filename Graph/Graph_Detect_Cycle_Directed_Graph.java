
/** 
Graph_Edge(int src, int dest, int wght){
        this.source=src;
        this.destination=dest;
        this.weight=wght;
    }
 */


 /**
  * 
  In This Program We Will Find Out That If There Exists A Cycle In The Directed Graph Or not
  */


import java.util.*;

public class Graph_Detect_Cycle_Directed_Graph{

    // for storing graph in form of adjacency list
    HashMap<Integer,ArrayList<Graph_Edge>> graph=new HashMap<>();
    ArrayList<Character> vertices;

    Graph_Detect_Cycle_Directed_Graph(ArrayList<Character> arr){
        this.vertices=arr;
    }

    // Add directed edge in a graph
    private void add_Directed_Edge(int src,int dest,int weight){
        Graph_Edge edge=new Graph_Edge(src,dest,weight);
        ArrayList<Graph_Edge> ar;
        if(this.graph.containsKey(src)){
            this.graph.get(src).add(edge);

        }
        else {
            ar=new ArrayList<>();
            ar.add(edge);
            this.graph.put(src,ar);
        }
        if(!this.graph.containsKey(dest)){
            this.graph.put(dest,new ArrayList<>());
        }
    }

    private void Adjacency_List(){
        for(Map.Entry<Integer,ArrayList<Graph_Edge>> itr:this.graph.entrySet()){
            System.out.print(this.vertices.get(itr.getKey())+" : ");
            for(Graph_Edge ed:itr.getValue()){
                System.out.print(this.vertices.get(ed.destination)+" ");
            }
            System.out.println();
        }
    }

    // function for detecting cycle in a graph
    private Boolean Cycle_Detect_In_Graph(){
        HashMap<Integer,Boolean> visited=new HashMap<>();
        HashMap<Integer,Boolean> recurs_Stack=new HashMap<>();

        for(Map.Entry<Integer,ArrayList<Graph_Edge>> it:this.graph.entrySet()){
            visited.put(it.getKey(),false);
            recurs_Stack.put(it.getKey(),false);
        }

        for(Map.Entry<Integer,ArrayList<Graph_Edge>> itr:this.graph.entrySet()){
            if(Cycle_Detect_Util(itr.getKey(),visited,recurs_Stack)){
                return true;
            }
        }
        return false;
    }
    // helping function for detecting cycle in graph
    private Boolean Cycle_Detect_Util(int key,HashMap<Integer,Boolean> visited,HashMap<Integer,Boolean> recurs_Stack){

        if(recurs_Stack.get(key)){
            // if node is already present in stack then there is a cycle
            return true;
        }

        if(visited.get(key)){
            return false;
        }

        visited.put(key,true);
        recurs_Stack.put(key,true);

        // Adjacent vertices
        for(Graph_Edge ed:this.graph.get(key)){
            if(Cycle_Detect_Util(ed.destination,visited,recurs_Stack)){
                return true;
            }
        }

        // Backtracking
        recurs_Stack.put(key,false);
        return false;


    }

    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        ArrayList<Character> chr=new ArrayList<>();
        int x=6;
        for(int i=0;i<x;i++){
            System.out.print("Enter "+(i+1)+" Vertex : ");
            chr.add(scan.next().charAt(0));
        }
        scan.close();
        Graph_Detect_Cycle_Directed_Graph gr=new Graph_Detect_Cycle_Directed_Graph(chr);
        gr.add_Directed_Edge(0,1,0);
        gr.add_Directed_Edge(0,5,0);
        gr.add_Directed_Edge(1,2,0);
        gr.add_Directed_Edge(1,3,0);
        gr.add_Directed_Edge(2,3,0);
        gr.add_Directed_Edge(3,4,0);
        gr.add_Directed_Edge(4,2,0);
        gr.add_Directed_Edge(5,1,0);

        gr.Adjacency_List();
        Boolean is_Cyclic=gr.Cycle_Detect_In_Graph();
        if(is_Cyclic){
            System.out.println("The Graph Contains Cycle");
        }
        else{
            System.out.println("This Graph Does Not Contains Cycle");
        }
    }
}
