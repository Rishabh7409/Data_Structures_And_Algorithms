
/** 
Graph_Edge(int src, int dest, int wght){
        this.source=src;
        this.destination=dest;
        this.weight=wght;
    }
 */


 /**
  * 
  In This Program We Will Find Out That If There Exists A Cycle In The Undirected Graph Or not
  */

import java.util.*;

public class Graph_Detect_Cycle_Undirected_Graph_BFS {

    private HashMap<Integer, ArrayList<Graph_Edge>> graph=new HashMap<>();
    private ArrayList<Character> vertices;

    Graph_Detect_Cycle_Undirected_Graph_BFS(ArrayList<Character> chr){
        this.vertices=chr;
    }

    private void add_Edge(int src,int dest,int weight){

        Graph_Edge ed=new Graph_Edge(src,dest,weight);
        ArrayList<Graph_Edge> ar;
        // Edge From Source To Destination
        if(this.graph.containsKey(src)){
            this.graph.get(src).add(ed);
        }
        else{
            ar=new ArrayList<>();
            ar.add(ed);
            this.graph.put(src,ar);
        }

        // Since it is undirected graph we also have to add an edge from destination back to source

        // Edge From Destination To Source
        Graph_Edge ed2=new Graph_Edge(dest,src,weight);
        if(this.graph.containsKey(dest)){
            this.graph.get(dest).add(ed2);
        }
        else{
            ar=new ArrayList<>();
            ar.add(ed2);
            this.graph.put(dest,ar);
        }
    }

    private void adjacency_list(){
        for(Map.Entry<Integer,ArrayList<Graph_Edge>> it:this.graph.entrySet()){
            System.out.print(this.vertices.get(it.getKey())+" : ");
            for(Graph_Edge ed:this.graph.get(it.getKey())){
                System.out.print(this.vertices.get(ed.destination)+" ");
            }
            System.out.println();
        }
    }

    //We Will Be Doing BFS Traversal
    private boolean Detect_Cycle_In_Graph(){
        //initialize visit of all nodes to -1
        //-1 : Unvisited
        //1 : Visited
        HashMap<Integer,Integer> visited=new HashMap<>();
        for(Map.Entry<Integer,ArrayList<Graph_Edge>> it:this.graph.entrySet()){
            visited.put(it.getKey(),-1);
        }

        Queue<Integer> queue=new LinkedList<>();
        //Start From Vertex 0
        queue.add(0);
        while (!queue.isEmpty()){
            int root=queue.remove();
            for(Graph_Edge ed:this.graph.get(root)){
                if(visited.get(ed.destination)==0){
                    //if This Vertex Is Also The Adjacent Node Of Another Vertex Then There Is A Cycle
                    return true;
                }
                if(!(queue.contains(ed.destination)) && visited.get(ed.destination)!=1){
                    //If This Vertex Is Not Added To Queue Till Now And  Is Not Visited
                    queue.add(ed.destination);
                    visited.put(ed.destination,0);
                }
            }
            visited.put(root,1); //Mark This Node As Visited
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ArrayList<Character> ar = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            System.out.print("Enter "+(i+1)+" Vertex: ");
            ar.add(scan.next().charAt(0));
        }
        scan.close();
        Graph_Detect_Cycle_Undirected_Graph_BFS gr = new Graph_Detect_Cycle_Undirected_Graph_BFS(ar);

        gr.add_Edge(0, 1, 0);
        gr.add_Edge(0, 2, 0);
        gr.add_Edge(1, 3, 0);
        gr.add_Edge(2,3,0);
        gr.add_Edge(1, 2, 0);
        gr.add_Edge(1, 4, 0);
        gr.add_Edge(3, 4, 0);

        gr.adjacency_list();
        System.out.println(gr.Detect_Cycle_In_Graph()?"This Graph Contains Cycle ":"This Graph Does Not Contain Cycle");
    }
}
