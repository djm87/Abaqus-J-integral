fname=fullfile(pwd,'odb','ThroughThicknessCrackInInfinitePlane.dat')

%positions (corner nodes) 
positions=[2.000000,1.900000,1.800000,1.700000,1.600000,1.500000,1.400000,1.300000,1.200000,1.100000,1.000000,0.900000,0.800000,0.700000,0.600000,0.500000,0.400000,0.300000,0.200000,0.100000]

%offset from step time to J
offset=13
%offset between slices
offsetSlice=3
%number of slices
nSlices=length(positions)*2-1

%number of contour levels
nContours=10;

JAll=zeros(nSlices,10)
c=textread(fname,'%s','delimiter','\n');

for i=1:length(c)
    line=c{i};
    if contains(line,'STEP TIME COMPLETED')
        lineId=i;
        tmp=strsplit(line);
        time=str2double(tmp{4})
        lineId=i+offset
        for j =1:nSlices
            lineId=i+offset+offsetSlice*(j-1)
            contourCnt=1;
            for k=0:offsetSlice-2
                line=c{lineId+k}
                tmp=strsplit(line);  
                for l=1:length(tmp)
                    val=str2double(tmp{l})
                    if and(~isnan(val),~isempty(val))
                       JAll(j,contourCnt)=val;
                       contourCnt=contourCnt+1;  
                    end
                end
            end
        end
%          JAll=flipud(JAll)
        %save frame to file
        fnameOut=sprintf('Js-Abaqus-at-time-%.3f',time)
        fnameOut=[strrep(fnameOut,'.','p'),'.txt']
        fileID = fopen(fnameOut,'w');
        cnt=0
        fprintf(fileID,'nan');
        for i=1:length(positions)
            fprintf(fileID,',%f',positions(i));
        end
        for i=1:nContours
            fprintf(fileID,'\n%d',i);
            for j=1:2:nSlices
                fprintf(fileID,',%16.10f',JAll(j,i));
            end
        end
        fclose(fileID);
        
        
    end
        
end