//Dijkstra Algorithm Is An Single Source Shortest Path Algorithm

 
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Graph_Dijkstra_Algorithm {

    HashMap<Integer,ArrayList<Graph_Edge>> graph=new HashMap<>();
    ArrayList<Character> vertices;

    Graph_Dijkstra_Algorithm(ArrayList<Character> ar){
        this.vertices=ar;

    }

    private void Add_Edge(int src,int dest,int weight){
        Graph_Edge ed=new Graph_Edge(src,dest,weight);
        if(this.graph.containsKey(src)){
            this.graph.get(src).add(ed);
        }
        else{
            ArrayList<Graph_Edge> ar=new ArrayList<>();
            ar.add(ed);
            this.graph.put(src,ar);
        }


        ed=new Graph_Edge(dest,src,weight);
        if(this.graph.containsKey(dest)){
            this.graph.get(dest).add(ed);
        }
        else{
            ArrayList<Graph_Edge> ar=new ArrayList<>();
            ar.add(ed);
            this.graph.put(dest,ar);
        }

    }

    private void Adjacency_List(){
        for(Map.Entry<Integer,ArrayList<Graph_Edge>> it:this.graph.entrySet()){
            System.out.print(this.vertices.get(it.getKey())+" : ");
            for(Graph_Edge ed:it.getValue()){
                System.out.print(this.vertices.get(ed.destination)+" ");
            }
            System.out.println();
        }
    }


    private void Dijkstra_Algorithm(int source){
        // for storing minimum distances
        HashMap<Integer,Integer> distance=new HashMap<>();

        // for storing visited nodes
        HashMap<Integer,Boolean> visited=new HashMap<>();

        // initialize all node's distances as inf and visited as false
        for(Map.Entry<Integer,ArrayList<Graph_Edge>> it:this.graph.entrySet()){
            distance.put(it.getKey(),Integer.MAX_VALUE);
            visited.put(it.getKey(),false);
        }

        // source vertex
        distance.put(source,0);
        visited.put(source,true);

        Queue<Integer> queue=new LinkedList<>();
        queue.add(source);
        while (!queue.isEmpty()){
            int current= queue.remove();
            // relax current vertex's adjacent vertices
            for(Graph_Edge ed:this.graph.get(current)){
                // if this vertex is not yet visited
                if(!queue.contains(ed.destination)&&!visited.get(ed.destination)){
                    queue.add(ed.destination);
                    visited.put(ed.destination,true);
                }
                // update distance if 
                //distance[adjacent vertex] > weight of edge+distance[current]
                distance.put(ed.destination,Math.min(distance.get(ed.destination),ed.weight+distance.get(current)));
            }
        }

        for(Map.Entry<Integer,Integer> it:distance.entrySet()){
            {
                System.out.println(source+" -> "+it.getKey()+" : "+it.getValue());

            }
        }
    }

    public static void main(String []args){
        Scanner scan=new Scanner(System.in);
        ArrayList<Character> ar=new ArrayList<>();
        for(int i=0;i<9;i++){
            System.out.print("Enter "+(i+1)+" vertex : ");
            ar.add(scan.next().charAt(0));
        }
        scan.close();

        Graph_Dijkstra_Algorithm gda=new Graph_Dijkstra_Algorithm(ar);

        gda.Add_Edge(0,1,4);
        gda.Add_Edge(0,4,8);
        gda.Add_Edge(1,2,8);
        gda.Add_Edge(1,4,11);
        gda.Add_Edge(2,3,7);
        gda.Add_Edge(2,8,2);
        gda.Add_Edge(2,6,4);
        gda.Add_Edge(3,7,9);
        gda.Add_Edge(3,6,14);
        gda.Add_Edge(4,5,1);
        gda.Add_Edge(4,8,7);
        gda.Add_Edge(5,6,2);
        gda.Add_Edge(5,8,6);
        gda.Add_Edge(6,7,10);

        gda.Adjacency_List();

        gda.Dijkstra_Algorithm(0);

    }

}
