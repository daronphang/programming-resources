## Persistent Volume Claim (PVC)

Storage request made by a user. Consumes PV resources rather than Node resources. Kubernetes searches for PVs that correspond to the PVCs' requested capacity and specified properties, so that each PVC can bind to a single PV.

PVCs are like tickets that authorize applications (Pods) to use them i.e. Pods use a PVC to claim access to the PV and start using it.

When there are multiple matches, can use labels and selectors to bind a PVC to a particular PV. This helps guard against a situation where a small PVC binds to a larger PV, as PV and PVCs have one-to-one relationship. **Remaining storage in the bound PVs are inaccessible to other users.**
