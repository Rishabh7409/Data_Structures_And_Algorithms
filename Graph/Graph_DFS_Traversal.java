
/** 
Graph_Edge(int src, int dest, int wght){
        this.source=src;
        this.destination=dest;
        this.weight=wght;
    }
 */


//  This Program is for Finding DFS of The Graph

import java.util.*;

public class Graph_DFS_Traversal {
    HashMap<Integer,ArrayList<Graph_Edge>> graph=new HashMap<>();
    ArrayList<Character> vertices;

    Graph_DFS_Traversal(ArrayList<Character> arr){
        this.vertices=arr;
    }

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

    void DFS_Traversal(){
        // For storing visited nodes
        HashMap<Integer,Boolean> visited=new HashMap<>();

        // initially all the vertices are unvisited
        for(Map.Entry<Integer,ArrayList<Graph_Edge>> it:this.graph.entrySet()){
            visited.put(it.getKey(),false);
        }

        // for stroing dfs traversal 
        ArrayList<Character> dfs=new ArrayList<>();
        for(Map.Entry<Integer,ArrayList<Graph_Edge>> itr:this.graph.entrySet()){
            if(!visited.get(itr.getKey())){
                DFS_Helper(dfs,visited,itr.getKey());
            }
        }
        System.out.println(dfs);
    }

    void DFS_Helper(ArrayList<Character> dfs,HashMap<Integer,Boolean> visited,int key){
        //add node to dfs
        dfs.add(this.vertices.get(key));
        // mark node as visited
        visited.put(key,true);
        // visit its adjacent vertex
        for(Graph_Edge ed:this.graph.get(key)){
            if(!visited.get(ed.destination)){
                DFS_Helper(dfs,visited,ed.destination);
            }
        }
    }

    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        ArrayList<Character> chr=new ArrayList<>();
        int x=6;
        for(int i=0;i<x;i++){
            System.out.print("Enter "+(i+1)+" Vertex: ");
            chr.add(scan.next().charAt(0));
        }
        scan.close();
        Graph_DFS_Traversal gr=new Graph_DFS_Traversal(chr);
        gr.add_Directed_Edge(1,2,0);
        gr.add_Directed_Edge(1,3,0);
        gr.add_Directed_Edge(3,4,0);
        gr.add_Directed_Edge(0,1,0);
        gr.add_Directed_Edge(0,5,0);
        gr.add_Directed_Edge(4,2,0);
        gr.add_Directed_Edge(5,1,0);

        gr.Adjacency_List();
        gr.DFS_Traversal();
    }
}
