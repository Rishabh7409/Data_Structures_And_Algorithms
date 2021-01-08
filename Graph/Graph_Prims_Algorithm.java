//A Spanning Tree Is A Subset Of A Graph Such That All The N Vertices Are Connected With Each Other With N-1 Edges..
//This Graph Is Completely ACyclic And If We Remove Any One Edge From Spanning Tree Then The Tree Will Be Disconnected..

//A Minimum Cost Spanning Tree Or Minimum Spanning Tree  Is A Spanning Tree With N-1 Edges With Least Weight
//In Minimum Spanning Tree If You Visit Two Vertices Through Some Weighted Edges Then That Will Be The Shortest Weight Between Those Two Vertices..

//Prim's Algorithm For Finding The Minimum Cost Spanning Tree :

//We Will Be Using Priority Queue For Prim's Algorithm

//1.Consider Three Arrays Or Hashmaps for storing
 //a.Visited Nodes
 //b.For Storing Parent Of Vertices(For Source It Will Be -1)
 //c.For Storing Distance Of Vertices

//2.Mark Source As Visited and Distance of Source As 0
//3.Make Source As Current
//4.Relax Adjacent Vertex Of Current Vertex And Add To Priority Queue Acc To Conditions




import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class Graph_Prims_Algorithm {

    ArrayList<Character> vertices;
    HashMap<Integer,ArrayList<Graph_Edge>> graph=new HashMap<>();

    Graph_Prims_Algorithm(ArrayList<Character> ver){
        this.vertices=ver;
    }

    //For Storing Pairs In Priority Queue Sorted According To Their Edge Weight
    static class Sort_Acc_Weight implements Comparator<Pair>{
        public int compare(Pair p1,Pair p2){
            return p1.weight-p2.weight;
        }

    }

    //Pair Which Will Be Stored In Priority Queue
    static class Pair{

        int value,weight;
        Pair(int val,int weight){
            this.value=val;
            this.weight=weight;  //Edge Weight
        }
    }

    private void Add_Edge(int src,int dest,int weight){
        Graph_Edge ed=new Graph_Edge(src,dest,weight);
        ArrayList<Graph_Edge> ar;

        //Edge From Source To Destination
        if(this.graph.containsKey(src)){
            this.graph.get(src).add(ed);
        }
        else {
            ar=new ArrayList<>();
            ar.add(ed);
            this.graph.put(src,ar);
        }

        //Edge From Destination To Source
        Graph_Edge ed2=new Graph_Edge(dest,src,weight);
        if(this.graph.containsKey(dest)){
            this.graph.get(dest).add(ed2);
        }
        else {
            ar=new ArrayList<>();
            ar.add(ed2);
            this.graph.put(dest,ar);
        }
    }

    private void Prims_Algorithm(int source,int n) {
        HashMap<Integer, Boolean> visited = new HashMap<>();  //For Storing Visited Vertices
        HashMap<Integer, Integer> parent = new HashMap<>();   //For Storing Parent of Vertices
        HashMap<Integer, Integer> weight = new HashMap<>();   //For Storing Weight Of The Vertices

        for (Map.Entry<Integer, ArrayList<Graph_Edge>> itr : this.graph.entrySet()) {
            visited.put(itr.getKey(), false);
            weight.put(itr.getKey(), Integer.MAX_VALUE);
        }

        PriorityQueue<Pair> queue = new PriorityQueue<>(new Sort_Acc_Weight());

        Pair start = new Pair(source, 0); //Starting Pair

        weight.put(source, 0); //Weight Of Source Vertex
        queue.add(start);     //Add This To Queue
        int ans = 0;
        //For Creating A Spanning Tree We Need N-1 Edges That's Why ans must not be greater than n-1
        while (ans != n-1 && !queue.isEmpty()) {
            Pair curr = queue.remove();

            if (!visited.get(curr.value)) { //If This Vertex Is Yet Not Visited
                visited.put(curr.value, true); //Mark This As Visited
                boolean flag = false;
                //Relaxation Of Adjacent Vertices
                for (Graph_Edge ed : this.graph.get(curr.value)) {
                    if (!visited.get(ed.destination)) {   //Relax If Adjacent Vertex Is Not Visited
                        if (weight.get(ed.destination) > ed.weight) { //Relax Only If Edge Weight Of Destination Is Greater Than Current Edge Weight
                            flag = true;
                            parent.put(ed.destination, curr.value); //Update Parent
                            weight.put(ed.destination, Math.min(ed.weight, weight.get(ed.destination))); //Update Edge Weight
                            queue.add(new Pair(ed.destination, ed.weight)); //Add This Pair To Priority Queue
                        }
                    }
                }
                if (flag) {
                    //If An Edge Is Created Then Increase ans
                    ans++;
                }
            }
        }
        Print_Minimum_Spanning_Tree(parent,weight,source);
    }


    //Method to Print The Vertices And Weight Of Spanning Tree Formed
    private void Print_Minimum_Spanning_Tree(HashMap<Integer,Integer> parent,HashMap<Integer,Integer> weight,int source){
        System.out.println("\nThe Minimum Cost Spanning Tree Formed Is:");
        System.out.println("\nSource\t"+"Destination\t"+"Weight\n");
        for (Map.Entry<Integer, Integer> itr : parent.entrySet()) {
            if (itr.getKey() != source) {
                System.out.println("\t"+itr.getValue()+"\t\t" + itr.getKey()+"\t\t\t" + weight.get(itr.getKey()));
            }
        }
    }

    // private void Adjacency_List(){
    //     for(Map.Entry<Integer,ArrayList<Graph_Edge>> itr:this.graph.entrySet()){
    //         System.out.print(itr.getKey()+" : ");
    //         for(Graph_Edge ed:itr.getValue()){
    //             System.out.print(ed.destination+" ");
    //         }
    //         System.out.println();
    //     }
    // }

    public static void main(String []args){
        ArrayList<Character> ar=new ArrayList<>();
        for(int i=0;i<6;i++){
            ar.add(Integer.toString(i).charAt(0));
        }

        Graph_Prims_Algorithm gpa=new Graph_Prims_Algorithm(ar);

        int n=9;
        int source=8;
        gpa.Add_Edge(0,1,4);
        gpa.Add_Edge(0,7,8);
        gpa.Add_Edge(1,2,8);
        gpa.Add_Edge(1,7,11);
        gpa.Add_Edge(2,3,7);
        gpa.Add_Edge(2,5,4);
        gpa.Add_Edge(2,8,2);
        gpa.Add_Edge(3,4,9);
        gpa.Add_Edge(3,5,14);
        gpa.Add_Edge(4,5,10);
        gpa.Add_Edge(5,6,2);
        gpa.Add_Edge(6,8,6);
        gpa.Add_Edge(6,7,1);
        gpa.Add_Edge(7,8,7);

//        gpa.Adjacency_List();

        gpa.Prims_Algorithm(source,n);

    }

}
