package src.test.java.com.dtw;

/*
 * BandTest.java   Jul 14, 2004
 *
 * Copyright (c) 2004 Stan Salvador
 * stansalvador@hotmail.com
 */



import src.main.java.com.timeseries.TimeSeries;
import src.main.java.com.util.BinaryDistance;
import src.main.java.com.util.DistanceFunction;
import src.main.java.com.util.DistanceFunctionFactory;
import src.main.java.com.util.EuclideanDistance;
import src.main.java.com.dtw.TimeWarpInfo;
import src.main.java.com.dtw.LinearWindow;

/**
 * @author Stan Salvador, stansalvador@hotmail.com
 * @since Jul 14, 2004
 */

public class BandTest
{

      // PUBLIC FUNCTIONS
      public static void main(String[] args)
      {
         if (args.length!=3 && args.length!=4)
         {
            System.out.println("USAGE:  java BandTest timeSeries1 timeSeries2 radius [EuclideanDistance|ManhattanDistance|BinaryDistance]");
            System.exit(1);
         }
         else
         {
            final TimeSeries tsI = new TimeSeries(args[0], false, false, ',');
            final TimeSeries tsJ = new TimeSeries(args[1], false, false, ',');
      
            final DistanceFunction distFn;
            if (args.length < 4)
            {
               distFn = DistanceFunctionFactory.getDistFnByName("EuclideanDistance"); 
            }
            else
            {
               distFn = DistanceFunctionFactory.getDistFnByName(args[3]);
            }   // end if
            
            final TimeWarpInfo info = src.main.java.com.dtw.DTW.getWarpInfoBetween(tsI, tsJ, new LinearWindow(tsI, tsJ, Integer.parseInt(args[2])), distFn);
            
            System.out.println("Warp Distance: " + info.getDistance());
            System.out.println("Warp Path:     " + info.getPath());
         }  // end if

      }  // end main()


}  // end class BandTest
