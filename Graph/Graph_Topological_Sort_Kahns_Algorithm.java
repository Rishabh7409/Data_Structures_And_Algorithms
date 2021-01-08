//This Is Kahn's Algorithm for finding The Topological Order Of A Directed Acyclic Graph..

//Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

//In This Algorithm We Find Out Topological Order Acc. to Indegrees Of The Vertices
//Indegree -- Number Of Edges Coming To The Vertex

//In Directed Acyclic Graph There Will Be At Least One Vertex Whose Indegree Will Be 0..
//In Directed Acyclic Graph There Will Be At Least One Vertex Whose Outdegree Will Be 0..

//Tech Dose
//Jenny Lectures


/*
    public class Graph_Edge
    {
        int source,destination,weight=0;

        Graph_Edge(int src, int dest, int wght){
            this.source=src;
            this.destination=dest;
            this.weight=wght;
        }
}
*/


import java.util.*;

public class Graph_Topological_Sort_Kahns_Algorithm {

    HashMap<Integer,ArrayList<Graph_Edge>>graph=new HashMap<>();
    ArrayList<Character> vertices;

    Graph_Topological_Sort_Kahns_Algorithm(ArrayList<Character> ar){
        this.vertices=ar;

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

    private void Topological_Ordering(){
        HashMap<Integer,Boolean> visited=new HashMap<>();  //visited state of the vertex
        HashMap<Integer,Integer> indegrees=new HashMap<>(); //indegrees of the vertices
        for(Map.Entry<Integer,ArrayList<Graph_Edge>> itr:this.graph.entrySet()){
            visited.put(itr.getKey(),false);
            if(!indegrees.containsKey(itr.getKey())){
                indegrees.put(itr.getKey(),0); //indegree of this will be 0 because this is a source vertex
            }
            for(Graph_Edge ed:itr.getValue()){
                visited.put(ed.destination,false);
                if(indegrees.containsKey(ed.destination)){
                    //incrementing the indegree value if already present
                    int val=indegrees.get(ed.destination);
                    indegrees.put(ed.destination,++val);
                }
                else{
                    //if not present then we will put 1 indegree
                    indegrees.put(ed.destination,1);
                }
            }
        }
        Topological_Ordering_Using_Kahn_Algorithm(visited,indegrees);
    }

    private void Topological_Ordering_Using_Kahn_Algorithm(HashMap<Integer,Boolean> visited,HashMap<Integer,Integer> indegrees){
        Queue<Integer> queue=new LinkedList<>();
        Stack<Character> topological=new Stack<>(); //for storing the topological order of graph
        int count=0;   //count of vertices in the queue
        for(Map.Entry<Integer,Integer> it:indegrees.entrySet()){
            //put all those nodes in queue whose indegree is 0 we will consider them as starting point of topological ordering..
            //This Is The Main Idea Behind The Kahn's Algorithm
            if(it.getValue()==0){
                queue.add(it.getKey());
            }
        }
        //loop until queue is not empty
        while (!queue.isEmpty()){
            int current=queue.remove();
            topological.add(this.vertices.get(current));
            count++;
            for(Graph_Edge ed:this.graph.get(current)){
                //After Visiting Current Vertex The Indegree Of Its Adjacent Vertex Will Be Decremented By 1
                int val=indegrees.get(ed.destination);
                val--;
                //If After Decrementing The Indegree Of Any Vertex Becomes 0 then Add This To Queue
                if(val==0){
                    if(!queue.contains(ed.destination)&&!visited.get(ed.destination)){
                        queue.add(ed.destination);
                        visited.put(ed.destination,true);
                    }
                }
                indegrees.put(ed.destination,val); //Update Indegree Of The Adjacent Vertex
            }
        }
        //if count is equal to total vertices then this means that the graph Is Completely Traversed And The
        //Topological Order Is Correct Otherwise Not
        int total_vertices=visited.size();
        if(count!=total_vertices){
            System.out.println("Topological Order Is Not Possible Because There Is Cycle In The Graph");
        }

//        System.out.println(topological+"\n\n"+count);

    }

    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        ArrayList<Character> ar=new ArrayList<>();
        for(int i=0;i<6;i++){
            ar.add(scan.next().charAt(0));
        }
        scan.close();

        Graph_Topological_Sort_Kahns_Algorithm gdp=new Graph_Topological_Sort_Kahns_Algorithm(ar);

        gdp.add_Directed_Edge(2,1,0);
        gdp.add_Directed_Edge(3,2,0);
        gdp.add_Directed_Edge(3,0,0);
        gdp.add_Directed_Edge(4,1,0);
        gdp.add_Directed_Edge(4,0,0);
        gdp.add_Directed_Edge(0,5,0);
        gdp.add_Directed_Edge(5,3,0);

        gdp.Adjacency_List();

        gdp.Topological_Ordering();
    }

}
