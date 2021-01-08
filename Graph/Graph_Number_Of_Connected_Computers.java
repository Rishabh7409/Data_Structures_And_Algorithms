//Tech Dose
//Leetcode -1319  --Making Wired Connections



import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Graph_Number_Of_Connected_Computers {
    HashMap<Integer,ArrayList<Graph_Edge>> graph=new HashMap<>();
    ArrayList<Character> vertices;

    Graph_Number_Of_Connected_Computers(ArrayList<Character> ar){
        this.vertices=ar;
    }

    private void Add_Edge(int src,int dest){
        Graph_Edge ed=new Graph_Edge(src,dest,0);
        if(this.graph.containsKey(src)){
            this.graph.get(src).add(ed);
        }
        else{
            ArrayList<Graph_Edge> ar=new ArrayList<>();
            ar.add(ed);
            this.graph.put(src,ar);
        }


        ed=new Graph_Edge(dest,src,0);
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

    private void Minimum_Number_Of_Edges(){
        //DO A DFS Traversal For Getting The Number of Connected Components in Graph   Visit Tech Dose For More Information(You Tube)

        HashMap<Integer,Boolean> visited=new HashMap<>();
        for(int i=0;i<graph.size();i++){
            visited.put(i,false);
        }
        int number_of_comp=0;
        for(Map.Entry<Integer,Boolean> it:visited.entrySet()){
            for(Graph_Edge ed:this.graph.get(it.getKey())){
                if(!visited.get(ed.destination)){
                    number_of_comp++;
                    DFS_Util(visited,ed.destination);
                }
            }
        }
        int total_edges=0;
        for (Map.Entry<Integer,ArrayList<Graph_Edge>> it:this.graph.entrySet()){
            total_edges+=it.getValue().size();  //Calculating Total Edges
        }

        total_edges/=2;  //Since This Is An directed Graph SO Total Edges Will Be total_Edges//2

        int redundant_edges=total_edges-((this.graph.size()-1)-(number_of_comp-1));  //Extra Edges Which Will Not Have Any Effect On Increasing The Number Of Components On Removing

        if(total_edges<this.graph.size()-1 || redundant_edges<number_of_comp-1){
            //total_edges<this.graph.size()-1 ::

            //If Total Edges Are Less Than Number If Vertices-1 Then All The Vertices Cannot Be Connected..
            //Acc. To MST N-1 Edges Are Required To Connect All The Vertices

            //redundant_edges<number_of_comp-1::

            // To Connect C Components We Need At Least C-1 Edges To Connect Them If Redundant Edges Are Less Than C-1(number of components-1) then The components cannot be connected

            System.out.println("Cannot Connect All The Computers");
        }
        else {
            //OtherWise We Can Use Redundant Edges To Connect All The Vertices Or Computers
            System.out.println("The Required Edges Are "+(number_of_comp-1));
        }
        System.out.println("The Number Of Components Are: "+number_of_comp);

    }

    private void DFS_Util(HashMap<Integer,Boolean> visited,int key){
        visited.put(key,true);
        for(Graph_Edge ed:this.graph.get(key)){
            if(!visited.get(ed.destination)){
                DFS_Util(visited,ed.destination);
            }
        }
    }

    public static void main(String []args){
        ArrayList<Character> ar=new ArrayList<>();
        Scanner scan=new Scanner(System.in);
        for(int i=0;i<6;i++){
            ar.add(scan.next().charAt(0));
        }
        scan.close();
        Graph_Number_Of_Connected_Computers gp=new Graph_Number_Of_Connected_Computers(ar);
        gp.Add_Edge(0,1);
        gp.Add_Edge(0,3);

//        gp.Add_Edge(3,2);
        gp.Add_Edge(1,2);
        gp.Add_Edge(4,5);
        gp.Add_Edge(2,3);
        gp.Adjacency_List();

        gp.Minimum_Number_Of_Edges();
    }

}
